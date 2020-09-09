// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

import * as fs from "@ts-common/fs"
import * as process from "process"
import * as path from "path"
import * as cm from "@ts-common/commonmark-to-markdown"
import * as it from "@ts-common/iterator"
import * as yaml from "js-yaml"

type Code = {
  readonly "input-file"?: ReadonlyArray<string>|string
}
const magic = `yaml $(tag) == 'all-api-versions' /* autogenerated */`;
const pathRegex = /microsoft\.(\w+)[\\\/]\S*[\\\/](\d{4}-\d{2}-\d{2}(|-preview))[\\\/]/i;

const main = async (specificationDir: string) => {
  try {
    const list = fs.recursiveReaddir(specificationDir)
    for await (const file of list) {
      const f = path.parse(file)
      if (f.base === "readme.md" && f.dir.endsWith('resource-manager')) {
        const original_content = (await fs.readFile(file)).toString()
        let content = original_content;
        const readMe = cm.parse(content)
        const set = new Set<string>()
        for (const c of cm.iterate(readMe.markDown)) {
          if (
            c.type === "code_block" &&
            c.info !== null &&
            (c.info.startsWith("yaml") && !c.info.startsWith(magic)) &&
            c.literal !== null
          ) {
            const DOC = (yaml.load(c.literal) as Code);
            if (DOC ) {
              const y = DOC['input-file']
              if (typeof y === "string") {
                set.add(y)
              } else if (it.isArray(y)) {
                for (const i of y) {
                  set.add(i)
                }
              }
            }
          }
        }
        let map = new Map<string, string[]>();
        for (let input of set) {
          let match = pathRegex.exec(input);
          if (!!match) {
            let tagName = `schema-${match[1].toLowerCase()}-${match[2]}`;
            if (!map.has(tagName)) {
              map.set(tagName, []);
            }
            let array = map.get(tagName);
            if (!!array) {
              array.push(input);
            }
          }
        }
        map = new Map(Array.from(map.entries()).sort().reverse());
        let schemaReadmeContent = 
`## AzureResourceSchema

These settings apply only when \`--azureresourceschema\` is specified on the command line.

### AzureResourceSchema multi-api

\`\`\` yaml $(azureresourceschema) && $(multiapi)
${yaml.dump({ 'batch': it.toArray(it.map(map.keys(), (tagName) => ({'tag': tagName})))}, { lineWidth: 1000})}
\`\`\`

Please also specify \`--azureresourceschema-folder=<path to the root directory of your azure-resource-manager-schemas clone>\`.
`
        map.forEach((inputList, tagName) => {
          schemaReadmeContent += 
`
### Tag: ${tagName} and azureresourceschema

\`\`\` yaml $(tag) == '${tagName}' && $(azureresourceschema)
output-folder: $(azureresourceschema-folder)/schemas

# all the input files in this apiVersion
${yaml.dump({ 'input-file': it.toArray(inputList)}, { lineWidth: 1000})}
\`\`\`
`
        });

        // content = content.replace( /``` yaml \$\(tag\) == 'all-api-versions' \/\* autogenerated \*\/[\S\s]*?```/g, '')
        // content = content.replace( /``` yaml \$\(tag\) == 'all-api-versions'[\S\s]*?```/g, '')
        // content = content.replace( /## Multi-API\/Profile support for AutoRest v3 generators[\S\s]*/g, '')

        // if(original_content !== content ){
        //   console.log(`Updating: ${file}`);
        //   fs.writeFile(path.join(f.dir, "readme.md"), content)
        // }

        console.log(`Rewriting: ${f.dir}/readme.azureresourceschema.md`);
        fs.writeFile(path.join(f.dir, "readme.azureresourceschema.md"), schemaReadmeContent);
        
      }
    }
  } catch (e) {
    console.error(e)
  }
}

main(path.join(process.cwd(), "specification"))

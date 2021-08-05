// <auto-generated>
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
//
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Azure.CognitiveServices.Language.LUIS.Authoring.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    public partial class PrebuiltDomainObject
    {
        /// <summary>
        /// Initializes a new instance of the PrebuiltDomainObject class.
        /// </summary>
        public PrebuiltDomainObject()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the PrebuiltDomainObject class.
        /// </summary>
        public PrebuiltDomainObject(string domainName = default(string), string modelName = default(string))
        {
            DomainName = domainName;
            ModelName = modelName;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "domain_name")]
        public string DomainName { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "model_name")]
        public string ModelName { get; set; }

    }
}

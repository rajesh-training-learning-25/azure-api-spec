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

    /// <summary>
    /// A prebuilt domain create object containing the name and culture of the
    /// domain.
    /// </summary>
    public partial class PrebuiltDomainCreateObject
    {
        /// <summary>
        /// Initializes a new instance of the PrebuiltDomainCreateObject class.
        /// </summary>
        public PrebuiltDomainCreateObject()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the PrebuiltDomainCreateObject class.
        /// </summary>
        /// <param name="domainName">The domain name.</param>
        /// <param name="culture">The culture of the new domain.</param>
        public PrebuiltDomainCreateObject(string domainName = default(string), string culture = default(string))
        {
            DomainName = domainName;
            Culture = culture;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets the domain name.
        /// </summary>
        [JsonProperty(PropertyName = "domainName")]
        public string DomainName { get; set; }

        /// <summary>
        /// Gets or sets the culture of the new domain.
        /// </summary>
        [JsonProperty(PropertyName = "culture")]
        public string Culture { get; set; }

    }
}

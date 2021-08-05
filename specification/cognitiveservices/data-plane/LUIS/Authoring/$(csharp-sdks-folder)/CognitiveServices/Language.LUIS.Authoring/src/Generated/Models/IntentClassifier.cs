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
    /// Intent Classifier.
    /// </summary>
    public partial class IntentClassifier : ModelInfo
    {
        /// <summary>
        /// Initializes a new instance of the IntentClassifier class.
        /// </summary>
        public IntentClassifier()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the IntentClassifier class.
        /// </summary>
        /// <param name="id">The ID of the Entity Model.</param>
        /// <param name="readableType">Possible values include: 'Entity
        /// Extractor', 'Child Entity Extractor', 'Hierarchical Entity
        /// Extractor', 'Hierarchical Child Entity Extractor', 'Composite
        /// Entity Extractor', 'List Entity Extractor', 'Prebuilt Entity
        /// Extractor', 'Intent Classifier', 'Pattern.Any Entity Extractor',
        /// 'Closed List Entity Extractor', 'Regex Entity Extractor'</param>
        /// <param name="name">Name of the Entity Model.</param>
        /// <param name="typeId">The type ID of the Entity Model.</param>
        /// <param name="customPrebuiltDomainName">The domain name.</param>
        /// <param name="customPrebuiltModelName">The intent name or entity
        /// name.</param>
        public IntentClassifier(System.Guid id, string readableType, string name = default(string), int? typeId = default(int?), string customPrebuiltDomainName = default(string), string customPrebuiltModelName = default(string))
            : base(id, readableType, name, typeId)
        {
            CustomPrebuiltDomainName = customPrebuiltDomainName;
            CustomPrebuiltModelName = customPrebuiltModelName;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets the domain name.
        /// </summary>
        [JsonProperty(PropertyName = "customPrebuiltDomainName")]
        public string CustomPrebuiltDomainName { get; set; }

        /// <summary>
        /// Gets or sets the intent name or entity name.
        /// </summary>
        [JsonProperty(PropertyName = "customPrebuiltModelName")]
        public string CustomPrebuiltModelName { get; set; }

        /// <summary>
        /// Validate the object.
        /// </summary>
        /// <exception cref="Rest.ValidationException">
        /// Thrown if validation fails
        /// </exception>
        public override void Validate()
        {
            base.Validate();
        }
    }
}

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
    /// Object model of an application version setting.
    /// </summary>
    public partial class AppVersionSettingObject
    {
        /// <summary>
        /// Initializes a new instance of the AppVersionSettingObject class.
        /// </summary>
        public AppVersionSettingObject()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the AppVersionSettingObject class.
        /// </summary>
        /// <param name="name">The application version setting name.</param>
        /// <param name="value">The application version setting value.</param>
        public AppVersionSettingObject(string name = default(string), string value = default(string))
        {
            Name = name;
            Value = value;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets the application version setting name.
        /// </summary>
        [JsonProperty(PropertyName = "name")]
        public string Name { get; set; }

        /// <summary>
        /// Gets or sets the application version setting value.
        /// </summary>
        [JsonProperty(PropertyName = "value")]
        public string Value { get; set; }

    }
}

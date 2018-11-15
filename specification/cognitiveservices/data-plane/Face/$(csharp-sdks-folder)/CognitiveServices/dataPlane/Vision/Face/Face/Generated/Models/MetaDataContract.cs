// <auto-generated>
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
//
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Azure.CognitiveServices.Vision.Face.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    /// <summary>
    /// A combination of user defined name and user specified data and
    /// recognition model name for largePersonGroup/personGroup, and
    /// largeFaceList/faceList.
    /// </summary>
    public partial class MetaDataContract : NameAndUserDataContract
    {
        /// <summary>
        /// Initializes a new instance of the MetaDataContract class.
        /// </summary>
        public MetaDataContract()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the MetaDataContract class.
        /// </summary>
        /// <param name="name">User defined name, maximum length is
        /// 128.</param>
        /// <param name="userData">User specified data. Length should not
        /// exceed 16KB.</param>
        public MetaDataContract(string name = default(string), string userData = default(string), string recognitionModel = default(string))
            : base(name, userData)
        {
            RecognitionModel = recognitionModel;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "RecognitionModel")]
        public string RecognitionModel { get; set; }

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

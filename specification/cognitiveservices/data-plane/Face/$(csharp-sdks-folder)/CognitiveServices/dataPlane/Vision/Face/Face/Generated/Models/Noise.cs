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
    /// Properties describing noise level of the image.
    /// </summary>
    public partial class Noise
    {
        /// <summary>
        /// Initializes a new instance of the Noise class.
        /// </summary>
        public Noise()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the Noise class.
        /// </summary>
        /// <param name="noiseLevel">An enum value indicating level of noise.
        /// Possible values include: 'Low', 'Medium', 'High'</param>
        /// <param name="value">A number indicating level of noise level
        /// ranging from 0 to 1. [0, 0.25) is under exposure. [0.25, 0.75) is
        /// good exposure. [0.75, 1] is over exposure. [0, 0.3) is low noise
        /// level. [0.3, 0.7) is medium noise level. [0.7, 1] is high noise
        /// level.</param>
        public Noise(NoiseLevel noiseLevel = default(NoiseLevel), double value = default(double))
        {
            NoiseLevel = noiseLevel;
            Value = value;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets an enum value indicating level of noise. Possible
        /// values include: 'Low', 'Medium', 'High'
        /// </summary>
        [JsonProperty(PropertyName = "noiseLevel")]
        public NoiseLevel NoiseLevel { get; set; }

        /// <summary>
        /// Gets or sets a number indicating level of noise level ranging from
        /// 0 to 1. [0, 0.25) is under exposure. [0.25, 0.75) is good exposure.
        /// [0.75, 1] is over exposure. [0, 0.3) is low noise level. [0.3, 0.7)
        /// is medium noise level. [0.7, 1] is high noise level.
        /// </summary>
        [JsonProperty(PropertyName = "value")]
        public double Value { get; set; }

    }
}

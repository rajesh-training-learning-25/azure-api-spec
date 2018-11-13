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
    using Microsoft.Rest;
    using Newtonsoft.Json;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;

    /// <summary>
    /// An array of face groups based on face similarity.
    /// </summary>
    public partial class GroupResult
    {
        /// <summary>
        /// Initializes a new instance of the GroupResult class.
        /// </summary>
        public GroupResult()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the GroupResult class.
        /// </summary>
        /// <param name="groups">A partition of the original faces based on
        /// face similarity. Groups are ranked by number of faces</param>
        /// <param name="messyGroup">Face ids array of faces that cannot find
        /// any similar faces from original faces.</param>
        public GroupResult(IList<IList<System.Guid>> groups, IList<System.Guid> messyGroup = default(IList<System.Guid>))
        {
            Groups = groups;
            MessyGroup = messyGroup;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets a partition of the original faces based on face
        /// similarity. Groups are ranked by number of faces
        /// </summary>
        [JsonProperty(PropertyName = "groups")]
        public IList<IList<System.Guid>> Groups { get; set; }

        /// <summary>
        /// Gets or sets face ids array of faces that cannot find any similar
        /// faces from original faces.
        /// </summary>
        [JsonProperty(PropertyName = "messyGroup")]
        public IList<System.Guid> MessyGroup { get; set; }

        /// <summary>
        /// Validate the object.
        /// </summary>
        /// <exception cref="ValidationException">
        /// Thrown if validation fails
        /// </exception>
        public virtual void Validate()
        {
            if (Groups == null)
            {
                throw new ValidationException(ValidationRules.CannotBeNull, "Groups");
            }
        }
    }
}

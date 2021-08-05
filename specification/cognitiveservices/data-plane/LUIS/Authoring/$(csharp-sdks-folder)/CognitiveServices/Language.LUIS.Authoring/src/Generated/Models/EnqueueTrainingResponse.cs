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
    /// Response model when requesting to train the model.
    /// </summary>
    public partial class EnqueueTrainingResponse
    {
        /// <summary>
        /// Initializes a new instance of the EnqueueTrainingResponse class.
        /// </summary>
        public EnqueueTrainingResponse()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the EnqueueTrainingResponse class.
        /// </summary>
        /// <param name="statusId">The train request status ID.</param>
        /// <param name="status">Possible values include: 'Queued',
        /// 'InProgress', 'UpToDate', 'Fail', 'Success'</param>
        public EnqueueTrainingResponse(int? statusId = default(int?), string status = default(string))
        {
            StatusId = statusId;
            Status = status;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets the train request status ID.
        /// </summary>
        [JsonProperty(PropertyName = "statusId")]
        public int? StatusId { get; set; }

        /// <summary>
        /// Gets or sets possible values include: 'Queued', 'InProgress',
        /// 'UpToDate', 'Fail', 'Success'
        /// </summary>
        [JsonProperty(PropertyName = "status")]
        public string Status { get; set; }

    }
}

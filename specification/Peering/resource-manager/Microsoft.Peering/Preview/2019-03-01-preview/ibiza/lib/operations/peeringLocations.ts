/*
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 *
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

import * as msRest from "@azure/ms-rest-js";
import * as Models from "../models";
import * as Mappers from "../models/peeringLocationsMappers";
import * as Parameters from "../models/parameters";
import { PeeringManagementClientContext } from "../peeringManagementClientContext";

/** Class representing a PeeringLocations. */
export class PeeringLocations {
  private readonly client: PeeringManagementClientContext;

  /**
   * Create a PeeringLocations.
   * @param {PeeringManagementClientContext} client Reference to the service client.
   */
  constructor(client: PeeringManagementClientContext) {
    this.client = client;
  }

  /**
   * Lists all of the available peering locations for the specified kind of peering.
   * @param kind The kind of the peering. Possible values include: 'Direct', 'Exchange'
   * @param [options] The optional parameters
   * @returns Promise<Models.PeeringLocationsListResponse>
   */
  list(kind: Models.Kind2, options?: msRest.RequestOptionsBase): Promise<Models.PeeringLocationsListResponse>;
  /**
   * @param kind The kind of the peering. Possible values include: 'Direct', 'Exchange'
   * @param callback The callback
   */
  list(kind: Models.Kind2, callback: msRest.ServiceCallback<Models.PeeringLocationListResult>): void;
  /**
   * @param kind The kind of the peering. Possible values include: 'Direct', 'Exchange'
   * @param options The optional parameters
   * @param callback The callback
   */
  list(kind: Models.Kind2, options: msRest.RequestOptionsBase, callback: msRest.ServiceCallback<Models.PeeringLocationListResult>): void;
  list(kind: Models.Kind2, options?: msRest.RequestOptionsBase | msRest.ServiceCallback<Models.PeeringLocationListResult>, callback?: msRest.ServiceCallback<Models.PeeringLocationListResult>): Promise<Models.PeeringLocationsListResponse> {
    return this.client.sendOperationRequest(
      {
        kind,
        options
      },
      listOperationSpec,
      callback) as Promise<Models.PeeringLocationsListResponse>;
  }
}

// Operation Specifications
const serializer = new msRest.Serializer(Mappers);
const listOperationSpec: msRest.OperationSpec = {
  httpMethod: "GET",
  path: "subscriptions/{subscriptionId}/providers/Microsoft.Peering/peeringLocations",
  urlParameters: [
    Parameters.subscriptionId
  ],
  queryParameters: [
    Parameters.kind,
    Parameters.apiVersion
  ],
  headerParameters: [
    Parameters.acceptLanguage
  ],
  responses: {
    200: {
      bodyMapper: Mappers.PeeringLocationListResult
    },
    default: {
      bodyMapper: Mappers.ErrorResponse
    }
  },
  serializer
};

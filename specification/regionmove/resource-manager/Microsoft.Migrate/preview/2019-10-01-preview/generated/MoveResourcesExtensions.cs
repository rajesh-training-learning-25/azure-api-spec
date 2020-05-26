// <auto-generated>
// MICROSOFT-MIT_NO_VERSION
// </auto-generated>

namespace regionmovecollection
{
    using Models;
    using System.Threading;
    using System.Threading.Tasks;

    /// <summary>
    /// Extension methods for MoveResources.
    /// </summary>
    public static partial class MoveResourcesExtensions
    {
            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            public static MoveResourceCollection Get(this IMoveResources operations, string resourceGroupName, string moveCollectionName)
            {
                return operations.GetAsync(resourceGroupName, moveCollectionName).GetAwaiter().GetResult();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task<MoveResourceCollection> GetAsync(this IMoveResources operations, string resourceGroupName, string moveCollectionName, CancellationToken cancellationToken = default(CancellationToken))
            {
                using (var _result = await operations.GetWithHttpMessagesAsync(resourceGroupName, moveCollectionName, null, cancellationToken).ConfigureAwait(false))
                {
                    return _result.Body;
                }
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            /// <param name='body'>
            /// </param>
            public static MoveResource Create(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName, MoveResource body = default(MoveResource))
            {
                return operations.CreateAsync(resourceGroupName, moveCollectionName, moveResourceName, body).GetAwaiter().GetResult();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            /// <param name='body'>
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task<MoveResource> CreateAsync(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName, MoveResource body = default(MoveResource), CancellationToken cancellationToken = default(CancellationToken))
            {
                using (var _result = await operations.CreateWithHttpMessagesAsync(resourceGroupName, moveCollectionName, moveResourceName, body, null, cancellationToken).ConfigureAwait(false))
                {
                    return _result.Body;
                }
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            public static void Delete(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName)
            {
                operations.DeleteAsync(resourceGroupName, moveCollectionName, moveResourceName).GetAwaiter().GetResult();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task DeleteAsync(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName, CancellationToken cancellationToken = default(CancellationToken))
            {
                (await operations.DeleteWithHttpMessagesAsync(resourceGroupName, moveCollectionName, moveResourceName, null, cancellationToken).ConfigureAwait(false)).Dispose();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            public static MoveResource Get1(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName)
            {
                return operations.Get1Async(resourceGroupName, moveCollectionName, moveResourceName).GetAwaiter().GetResult();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task<MoveResource> Get1Async(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName, CancellationToken cancellationToken = default(CancellationToken))
            {
                using (var _result = await operations.Get1WithHttpMessagesAsync(resourceGroupName, moveCollectionName, moveResourceName, null, cancellationToken).ConfigureAwait(false))
                {
                    return _result.Body;
                }
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            /// <param name='body'>
            /// </param>
            public static MoveResource Update(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName, UpdateMoveResourceRequest body = default(UpdateMoveResourceRequest))
            {
                return operations.UpdateAsync(resourceGroupName, moveCollectionName, moveResourceName, body).GetAwaiter().GetResult();
            }

            /// <param name='operations'>
            /// The operations group for this extension method.
            /// </param>
            /// <param name='resourceGroupName'>
            /// </param>
            /// <param name='moveCollectionName'>
            /// </param>
            /// <param name='moveResourceName'>
            /// </param>
            /// <param name='body'>
            /// </param>
            /// <param name='cancellationToken'>
            /// The cancellation token.
            /// </param>
            public static async Task<MoveResource> UpdateAsync(this IMoveResources operations, string resourceGroupName, string moveCollectionName, string moveResourceName, UpdateMoveResourceRequest body = default(UpdateMoveResourceRequest), CancellationToken cancellationToken = default(CancellationToken))
            {
                using (var _result = await operations.UpdateWithHttpMessagesAsync(resourceGroupName, moveCollectionName, moveResourceName, body, null, cancellationToken).ConfigureAwait(false))
                {
                    return _result.Body;
                }
            }

    }
}

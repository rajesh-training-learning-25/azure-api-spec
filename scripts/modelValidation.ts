// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License in the project root for license information.

import { modelValidation } from '@azure/rest-api-specs-scripts'

modelValidation.main().catch(e => { console.log(e); process.exit(1); })

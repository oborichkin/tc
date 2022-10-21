server = {
    "version": "2019.2.4 (build 72059)",
    "versionMajor": 2019,
    "versionMinor": 2,
    "startTime": "20200805T190912+0300",
    "currentTime": "20201107T224939+0300",
    "buildNumber": "72059",
    "buildDate": "20200508T000000+0300",
    "internalId": "f5f45726-88a4-4366-b340-563da2e51407",
    "webUrl": "https://teamcity.com",
    "projects": {
        "href": "/app/rest/projects"
    },
    "vcsRoots": {
        "href": "/app/rest/vcs-roots"
    },
    "builds": {
        "href": "/app/rest/builds"
    },
    "users": {
        "href": "/app/rest/users"
    },
    "userGroups": {
        "href": "/app/rest/userGroups"
    },
    "agents": {
        "href": "/app/rest/agents"
    },
    "buildQueue": {
        "href": "/app/rest/buildQueue"
    },
    "agentPools": {
        "href": "/app/rest/agentPools"
    },
    "investigations": {
        "href": "/app/rest/investigations"
    },
    "mutes": {
        "href": "/app/rest/mutes"
    }
}

projects = {
    "count": 693,
    "href": "/app/rest/projects",
    "project": [
        {
            "id": "_Root",
            "name": "<Root project>",
            "description": "Contains all other projects",
            "href": "/app/rest/projects/id:_Root",
            "webUrl": "https://teamcity.com/project.html?projectId=_Root"
        },
        {
            "id": "Abc",
            "name": "ABC",
            "parentProjectId": "_Root",
            "description": "ABC Project",
            "href": "/app/rest/projects/id:Abc",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc"
        },
        {
            "id": "Abc_Dependencies",
            "name": "Dependencies",
            "parentProjectId": "Abc",
            "description": "ABC Dependencies",
            "href": "/app/rest/projects/id:Abc_Dependencies",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies"
        },
        {
            "id": "Abc_Dependencies_First",
            "name": "First Dependency",
            "parentProjectId": "Abc_Dependencies",
            "href": "/app/rest/projects/id:Abc_Dependencies_First",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies_First"
        },
        {
            "id": "Abc_Dependencies_Second",
            "name": "Second Dependency",
            "parentProjectId": "Abc_Dependencies",
            "href": "/app/rest/projects/id:Abc_Dependencies_Second",
            "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies_Second"
        }
    ]
}

project = {
    "id": "Abc",
    "name": "ABC",
    "parentProjectId": "_Root",
    "description": "ABC",
    "href": "/app/rest/projects/id:Abc",
    "webUrl": "https://teamcity.com/project.html?projectId=Abc",
    "parentProject": {
        "id": "_Root",
        "name": "<Root project>",
        "description": "Contains all other projects",
        "href": "/app/rest/projects/id:_Root",
        "webUrl": "https://teamcity.com/project.html?projectId=_Root"
    },
    "buildTypes": {
        "count": 9,
        "buildType": [
            {
                "id": "Abc_Master",
                "name": "master",
                "description": "ABC master branch build",
                "projectName": "ABC",
                "projectId": "Abc",
                "href": "/app/rest/buildTypes/id:Abc_Master",
                "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Master"
            },
            {
                "id": "Abc_Build",
                "name": "build",
                "description": "ABC non-master branch builds",
                "projectName": "ABC",
                "projectId": "Abc",
                "href": "/app/rest/buildTypes/id:Abc_Build",
                "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Build"
            },
            {
                "id": "Abc_Release",
                "name": "release",
                "description": "release ABC builds",
                "projectName": "ABC",
                "projectId": "Abc",
                "href": "/app/rest/buildTypes/id:Abc_Release",
                "webUrl": "https://teamcity.com/viewType.html?buildTypeId=Abc_Release"
            }
        ]
    },
    "projects": {
        "count": 3,
        "project": [
            {
                "id": "Abc_Dependencies",
                "name": "Dependencies",
                "parentProjectId": "Abc",
                "description": "ABC Dependencies",
                "href": "/app/rest/projects/id:Abc_Dependencies",
                "webUrl": "https://teamcity.com/project.html?projectId=Abc_Dependencies"
            },
            {
                "id": "Abc_Packages",
                "name": "Packages",
                "parentProjectId": "Abc",
                "description": "ABC Packages",
                "href": "/app/rest/projects/id:Abc_Packages",
                "webUrl": "https://teamcity.com/project.html?projectId=Abc_Packages"
            },
            {
                "id": "Abc_Tests",
                "name": "Tests",
                "parentProjectId": "Abc",
                "description": "ABC Tests",
                "href": "/app/rest/projects/id:Abc_Tests",
                "webUrl": "https://teamcity.com/project.html?projectId=Abc_Tests"
            }
        ]
    }
}

vcs_roots = {
    "count": 10,
    "href": "/app/rest/vcs-roots?locator=count:10",
    "nextHref": "/app/rest/vcs-roots?locator=count:10,start:10",
    "vcs-root": [
        {
            "id": "Abc",
            "name": "ABC",
            "href": "/app/rest/vcs-roots/id:Abc"
        },
        {
            "id": "Abc1_2",
            "name": "ABC (1)",
            "href": "/app/rest/vcs-roots/id:Abc1_2"
        },
        {
            "id": "Abc2",
            "name": "ABC (2)",
            "href": "/app/rest/vcs-roots/id:Abc2"
        },
        {
            "id": "AbcCi",
            "name": "ABC CI",
            "href": "/app/rest/vcs-roots/id:AbcCi"
        },
        {
            "id": "Abc_Packages_AbcPackages",
            "name": "ABC packages",
            "href": "/app/rest/vcs-roots/id:Abc_Packages_AbcPackages"
        },
        {
            "id": "Abc_Packages_AbcPackages1",
            "name": "ABC packages (1)",
            "href": "/app/rest/vcs-roots/id:Abc_Packages_AbcPackages1"
        },
        {
            "id": "Abc_Packages_AbcPackages2",
            "name": "ABC packages (2)",
            "href": "/app/rest/vcs-roots/id:Abc_Packages_AbcPackages2"
        },
        {
            "id": "Abc1",
            "name": "ABC release",
            "href": "/app/rest/vcs-roots/id:Abc1"
        },
        {
            "id": "Abc_Tests_AbcTestMaster",
            "name": "ABC Test Master",
            "href": "/app/rest/vcs-roots/id:Abc_Tests_AbcTestMaster"
        },
        {
            "id": "Abc_Tests_AbcTestDefault",
            "name": "ABC Test Default",
            "href": "/app/rest/vcs-roots/id:Abc_Tests_AbcTestDefault"
        }
    ]
}

vcs_root = {
    "id": "Abc_Abc",
    "name": "ABC",
    "vcsName": "jetbrains.git",
    "modificationCheckInterval": 60,
    "href": "/app/rest/vcs-roots/id:Abc_Abc",
    "project": {
        "id": "Abc",
        "name": "ABC",
        "parentProjectId": "_Root",
        "description": "This is  ABC",
        "href": "/app/rest/projects/id:Abc",
        "webUrl": "https://teamcity.com/project.html?projectId=Abc"
    },
    "properties": {
        "count": 11,
        "property": [
            {
                "name": "agentCleanFilesPolicy",
                "value": "ALL_UNTRACKED"
            },
            {
                "name": "agentCleanPolicy",
                "value": "ON_BRANCH_CHANGE"
            },
            {
                "name": "authMethod",
                "value": "TEAMCITY_SSH_KEY"
            },
            {
                "name": "branch",
                "value": "master"
            },
            {
                "name": "ignoreKnownHosts",
                "value": "true"
            },
            {
                "name": "submoduleCheckout",
                "value": "CHECKOUT"
            },
            {
                "name": "teamcity:branchSpec",
                "value": "+:refs/heads/*"
            },
            {
                "name": "teamcitySshKey",
                "value": "GitLab Public Deploy Key"
            },
            {
                "name": "url",
                "value": "git@github.com:ABC/ABC.git"
            },
            {
                "name": "useAlternates",
                "value": "true"
            },
            {
                "name": "usernameStyle",
                "value": "USERID"
            }
        ]
    },
    "vcsRootInstances": {
        "href": "/app/rest/vcs-root-instances?locator=vcsRoot:(id:Abc_Abc)"
    }
}

builds = {
    "count": 10,
    "href": "/app/rest/buildTypes/id:Abc_Master/builds/?locator=start:0,count:10",
    "nextHref": "/app/rest/buildTypes/id:Abc_Master/builds/?locator=start:10,count:10",
    "build": [
        {
            "id": 1316053,
            "buildTypeId": "Abc_Master",
            "number": "570",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1316053",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1316053&buildTypeId=Abc_Master"
        },
        {
            "id": 1315981,
            "buildTypeId": "Abc_Master",
            "number": "569",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1315981",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1315981&buildTypeId=Abc_Master"
        },
        {
            "id": 1315290,
            "buildTypeId": "Abc_Master",
            "number": "568",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1315290",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1315290&buildTypeId=Abc_Master"
        },
        {
            "id": 1314277,
            "buildTypeId": "Abc_Master",
            "number": "567",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1314277",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1314277&buildTypeId=Abc_Master"
        },
        {
            "id": 1313577,
            "buildTypeId": "Abc_Master",
            "number": "566",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1313577",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1313577&buildTypeId=Abc_Master"
        },
        {
            "id": 1312998,
            "buildTypeId": "Abc_Master",
            "number": "565",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312998",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312998&buildTypeId=Abc_Master"
        },
        {
            "id": 1312365,
            "buildTypeId": "Abc_Master",
            "number": "564",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312365",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312365&buildTypeId=Abc_Master"
        },
        {
            "id": 1312249,
            "buildTypeId": "Abc_Master",
            "number": "563",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312249",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312249&buildTypeId=Abc_Master"
        },
        {
            "id": 1312166,
            "buildTypeId": "Abc_Master",
            "number": "562",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1312166",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1312166&buildTypeId=Abc_Master"
        },
        {
            "id": 1311678,
            "buildTypeId": "Abc_Master",
            "number": "561",
            "status": "SUCCESS",
            "state": "finished",
            "branchName": "master",
            "defaultBranch": True,
            "href": "/app/rest/builds/id:1311678",
            "webUrl": "https://teamcity.com/viewLog.html?buildId=1311678&buildTypeId=Abc_Master"
        }
    ]
}

vcs_root_instances = {
    "count": 1,
    "href": "/app/rest/vcs-root-instances?locator=vcsRoot:(id:Abc_Abc)",
    "vcs-root-instance": [
        {
            "id": "2476",
            "vcs-root-id": "Abc_Abc",
            "name": "ABC",
            "href": "/app/rest/vcs-root-instances/id:2476"
        }
    ]
}

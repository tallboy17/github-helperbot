Repository: apache/airflow
Language: Python
Stars: 40629
Forks: 15180
-----
Often you will see an issue that is assigned to specific milestone with Airflow version, or a PR that gets merged
to the main branch and you might wonder which release the merged PR(s) will be released in or which release the fixed
issues will be in. The answer to this is as usual - it depends on various scenarios. The answer is different for PRs and Issues.  
To add a bit of context, we are following the [Semver](https://semver.org/) versioning scheme as described in
[Airflow release process](https://airflow.apache.org/docs/apache-airflow/stable/release-process.html). More
details are explained in detail in this README under the [Semantic versioning](#semantic-versioning) chapter, but
in short, we have `MAJOR.MINOR.PATCH` versions of Airflow.  
* `MAJOR` version is incremented in case of breaking changes
* `MINOR` version is incremented when there are new features added
* `PATCH` version is incremented when there are only bug-fixes and doc-only changes  
Generally we release `MINOR` versions of Airflow from a branch that is named after the MINOR version. For example
`2.7.*` releases are released from `v2-7-stable` branch, `2.8.*` releases are released from `v2-8-stable`
branch, etc.  
1. Most of the time in our release cycle, when the branch for next `MINOR` branch is not yet created, all
PRs merged to `main` (unless they get reverted), will find their way to the next `MINOR` release. For example
if the last release is `2.7.3` and `v2-8-stable` branch is not created yet, the next `MINOR` release
is `2.8.0` and all PRs merged to main will be released in `2.8.0`. However, some PRs (bug-fixes and
doc-only changes) when merged, can be cherry-picked to current `MINOR` branch and released in the
next `PATCHLEVEL` release. For example, if `2.8.1` is already released and we are working on `2.9.0dev`,  then
marking a PR with `2.8.2` milestone means that it will be cherry-picked to `v2-8-test` branch and
released in `2.8.2rc1`, and eventually in `2.8.2`.  
2. When we prepare for the next `MINOR` release, we cut new `v2-*-test` and `v2-*-stable` branch
and prepare `alpha`, `beta` releases for the next `MINOR` version, the PRs merged to main will still be
released in the next `MINOR` release until `rc` version is cut. This is happening because the `v2-*-test`
and `v2-*-stable` branches are rebased on top of main when next `beta` and `rc` releases are prepared.
For example, when we cut `2.10.0beta1` version, anything merged to main before `2.10.0rc1` is released,
will find its way to 2.10.0rc1.  
3. Then, once we prepare the first RC candidate for the MINOR release, we stop moving the `v2-*-test` and
`v2-*-stable` branches and the PRs merged to main will be released in the next `MINOR` release.
However, some PRs (bug-fixes and doc-only changes) when merged, can be cherry-picked to current `MINOR`
branch and released in the next `PATCHLEVEL` release - for example when the last released version from `v2-10-stable`
branch is `2.10.0rc1`, some of the PRs from main can be marked as `2.10.0` milestone by committers,
the release manager will try to cherry-pick them into the release branch.
If successful, they will be released in `2.10.0rc2` and subsequently in `2.10.0`. This also applies to
subsequent `PATCHLEVEL` versions. When for example `2.10.1` is already released, marking a PR with
`2.10.2` milestone will mean that it will be cherry-picked to `v2-10-stable` branch and released in `2.10.2rc1`
and eventually in `2.10.2`.  
The final decision about cherry-picking is made by the release manager.  
Marking issues with a milestone is a bit different. Maintainers do not mark issues with a milestone usually,
normally they are only marked in PRs. If PR linked to the issue (and "fixing it") gets merged and released
in a specific version following the process described above, the issue will be automatically closed, no
milestone will be set for the issue, you need to check the PR that fixed the issue to see which version
it was released in.  
However, sometimes maintainers mark issues with specific milestone, which means that the
issue is important to become a candidate to take a look when the release is being prepared. Since this is an
Open-Source project, where basically all contributors volunteer their time, there is no guarantee that specific
issue will be fixed in specific version. We do not want to hold the release because some issue is not fixed,
so in such case release manager will reassign such unfixed issues to the next milestone in case they are not
fixed in time for the current release. Therefore, the milestone for issue is more of an intent that it should be
looked at, than promise it will be fixed in the version.  
More context and **FAQ** about the patchlevel release can be found in the
[What goes into the next release](dev/WHAT_GOES_INTO_THE_NEXT_RELEASE.md) document in the `dev` folder of the
repository.
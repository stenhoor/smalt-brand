# Work in progress

<p><img class="sw-light" src="/media/badges/work-in-progress.svg" alt="Work in progress. Come build with us." height="56"><img class="sw-dark" src="/media/badges/work-in-progress-on-dark.svg" alt="Work in progress. Come build with us." height="56"></p>

**Come build with us.** Everything in the smalt family is before 1.0: it works, it's moving fast, and it will change.
That's the point of this stage. We'd rather find the right design with you than lock in the wrong one.

## Who it's for

- **For** people who like trying new things, don't mind breaking changes, and want a say in how it turns out.
- **Not yet for** production, or for data you can't recreate.

## What can change

Before 1.0, any release can change:

- **The API:** names, arguments and results, in any package.
- **The file format:** a new release may not open a database written by an older one, and we won't always provide a way
  to migrate it.
- **Behaviour:** query results can change when a bug is fixed or a rule is made stricter.

## How you'll hear

Every release's notes start with a **Breaking** section, even when it says "None", so you can see at a glance whether
an upgrade needs care.

## What to do

- **Pin exact versions** (`npm install --save-exact`) and upgrade on purpose, after reading **Breaking**.
- **Keep your source data,** so you can rebuild a database if a new release can't open it.
- **Tell us what broke,** and what you wish worked differently: open an issue on the project it's about (the list is on
  [Get involved](/community/get-involved)).

Plink
=====

A storage for links similar to del.icio.us using Tornado and Motor (async mongo engine) striving for great concurrency of users.

Requirements
------------

* [Tornado](http://tornadoweb.org)
* [Motor](https://github.com/mongodb/motor/)


Design
------

Plink will be an Api representing most of the CRUD of a link database, with a layer of html+js to ease managing and viewing.

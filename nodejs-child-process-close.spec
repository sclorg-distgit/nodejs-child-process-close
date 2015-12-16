%{?scl:%scl_package nodejs-child-process-close}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-child-process-close
Version:        0.1.1
Release:        3.2.sc1%{?dist}
Summary:        Make child_process objects emit 'close' events
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          Development/Libraries
#MIT license included in README file
License:        MIT
URL:            https://github.com/piscisaureus/child-process-close
Source0:        http://registry.npmjs.org/child-process-close/-/child-process-close-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
This module makes child process objects, (created with spawn, fork, exec or 
execFile) emit the close event in node v0.6 like they do in node v0.8. This 
makes it easier to write code that works correctly on both versions of node.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/child-process-close
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/child-process-close

%nodejs_symlink_deps

%check
%{?scl:scl enable %{scl} "}
%{__nodejs} test/test.js
%{?scl:"}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/child-process-close
%doc README.md

%changelog
* Thu Nov 07 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-3.2
- enable scl when running tests

* Wed Nov 06 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-3.1
- add software collections suport

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.1-2
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.1-1
- initial package

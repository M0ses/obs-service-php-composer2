#
# spec file for package obs-service-php-composer2
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define obs_service_dir /usr/lib/obs/service/

Name:           obs-service-php-composer2
Version:        0.0.1
Release:        0
Summary:	OBS service for fetching php requirements with php-composer2
License:        GPL-3.0
URL:            https://github.com/M0ses/obs-service-php-composer2
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  php-composer2
Requires:  php-composer2

%description
OBS service for fetching php requirements with php-composer2.

%prep
%autosetup

%build

%install
%make_install

%post
%postun

%files
#%license COPYING
#%doc ChangeLog README
%dir /usr/lib/obs
%dir /usr/lib/obs/service
%{obs_service_dir}/php-composer2
%{obs_service_dir}/php-composer2.service

%changelog


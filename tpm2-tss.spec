#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tpm2-tss
Version  : 3.2.0
Release  : 14
URL      : https://github.com/tpm2-software/tpm2-tss/archive/3.2.0/tpm2-tss-3.2.0.tar.gz
Source0  : https://github.com/tpm2-software/tpm2-tss/archive/3.2.0/tpm2-tss-3.2.0.tar.gz
Summary  : Library to simplify management of TCTIs.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: tpm2-tss-config = %{version}-%{release}
Requires: tpm2-tss-lib = %{version}-%{release}
Requires: tpm2-tss-license = %{version}-%{release}
Requires: tpm2-tss-man = %{version}-%{release}
BuildRequires : acl-bin
BuildRequires : autoconf-archive-dev
BuildRequires : doxygen
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : perl
BuildRequires : pkgconfig(cmocka)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libcurl)
BuildRequires : valgrind

%description
[![Build Status](https://github.com/tpm2-software/tpm2-tss/workflows/CI/badge.svg)](https://github.com/tpm2-software/tpm2-tss/actions)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/1bqv1y7rntqiewln?svg=true)](https://ci.appveyor.com/project/williamcroberts/tpm2-tss)
[![FreeBSD Build status](https://api.cirrus-ci.com/github/tpm2-software/tpm2-tss.svg?branch=master)](https://cirrus-ci.com/github/tpm2-software/tpm2-tss)
[![Coverity Scan](https://img.shields.io/coverity/scan/3997.svg)](https://scan.coverity.com/projects/tpm2-tss)
[![Coverage Status](https://codecov.io/gh/tpm2-software/tpm2-tss/branch/master/graph/badge.svg)](https://codecov.io/gh/tpm2-software/tpm2-tss)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2332/badge)](https://bestpractices.coreinfrastructure.org/projects/2332)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/tpm2-software/tpm2-tss.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tpm2-software/tpm2-tss/alerts/)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/tpm2-software/tpm2-tss.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tpm2-software/tpm2-tss/context:cpp)
[![Documentation Status](https://readthedocs.org/projects/tpm2-tss/badge/?version=latest)](https://tpm2-tss.readthedocs.io/en/latest/?badge=latest)
[![Fuzzing Status](https://oss-fuzz-build-logs.storage.googleapis.com/badges/tpm2-tss.svg)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:tpm2-tss)
[![Gitter](https://badges.gitter.im/tpm2-software/community.svg)](https://gitter.im/tpm2-software/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

%package config
Summary: config components for the tpm2-tss package.
Group: Default

%description config
config components for the tpm2-tss package.


%package dev
Summary: dev components for the tpm2-tss package.
Group: Development
Requires: tpm2-tss-lib = %{version}-%{release}
Provides: tpm2-tss-devel = %{version}-%{release}
Requires: tpm2-tss = %{version}-%{release}

%description dev
dev components for the tpm2-tss package.


%package lib
Summary: lib components for the tpm2-tss package.
Group: Libraries
Requires: tpm2-tss-license = %{version}-%{release}

%description lib
lib components for the tpm2-tss package.


%package license
Summary: license components for the tpm2-tss package.
Group: Default

%description license
license components for the tpm2-tss package.


%package man
Summary: man components for the tpm2-tss package.
Group: Default

%description man
man components for the tpm2-tss package.


%prep
%setup -q -n tpm2-tss-3.2.0
cd %{_builddir}/tpm2-tss-3.2.0

%build
## build_prepend content
./bootstrap
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645218848
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%reconfigure --disable-static --with-udevrulesdir=/usr/lib/udev/rules.d --disable-dependency-tracking
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1645218848
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tpm2-tss
cp %{_builddir}/tpm2-tss-3.2.0/LICENSE %{buildroot}/usr/share/package-licenses/tpm2-tss/af62924ad3089277c413ea767486f404ac159ce1
%make_install

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/tpm-udev.rules

%files dev
%defattr(-,root,root,-)
/usr/include/tss2/tss2_common.h
/usr/include/tss2/tss2_esys.h
/usr/include/tss2/tss2_fapi.h
/usr/include/tss2/tss2_mu.h
/usr/include/tss2/tss2_rc.h
/usr/include/tss2/tss2_sys.h
/usr/include/tss2/tss2_tcti.h
/usr/include/tss2/tss2_tcti_cmd.h
/usr/include/tss2/tss2_tcti_device.h
/usr/include/tss2/tss2_tcti_mssim.h
/usr/include/tss2/tss2_tcti_pcap.h
/usr/include/tss2/tss2_tcti_swtpm.h
/usr/include/tss2/tss2_tctildr.h
/usr/include/tss2/tss2_tpm2_types.h
/usr/lib64/libtss2-esys.so
/usr/lib64/libtss2-fapi.so
/usr/lib64/libtss2-mu.so
/usr/lib64/libtss2-rc.so
/usr/lib64/libtss2-sys.so
/usr/lib64/libtss2-tcti-cmd.so
/usr/lib64/libtss2-tcti-device.so
/usr/lib64/libtss2-tcti-mssim.so
/usr/lib64/libtss2-tcti-pcap.so
/usr/lib64/libtss2-tcti-swtpm.so
/usr/lib64/libtss2-tctildr.so
/usr/lib64/pkgconfig/tss2-esys.pc
/usr/lib64/pkgconfig/tss2-fapi.pc
/usr/lib64/pkgconfig/tss2-mu.pc
/usr/lib64/pkgconfig/tss2-rc.pc
/usr/lib64/pkgconfig/tss2-sys.pc
/usr/lib64/pkgconfig/tss2-tcti-cmd.pc
/usr/lib64/pkgconfig/tss2-tcti-device.pc
/usr/lib64/pkgconfig/tss2-tcti-mssim.pc
/usr/lib64/pkgconfig/tss2-tcti-pcap.pc
/usr/lib64/pkgconfig/tss2-tcti-swtpm.pc
/usr/lib64/pkgconfig/tss2-tctildr.pc
/usr/share/man/man3/ESYS_CONTEXT.3
/usr/share/man/man3/ESYS_TR.3
/usr/share/man/man3/ESYS_TR_defines.3
/usr/share/man/man3/Esys_ActivateCredential.3
/usr/share/man/man3/Esys_Certify.3
/usr/share/man/man3/Esys_CertifyCreation.3
/usr/share/man/man3/Esys_ChangeEPS.3
/usr/share/man/man3/Esys_ChangePPS.3
/usr/share/man/man3/Esys_Clear.3
/usr/share/man/man3/Esys_ClearControl.3
/usr/share/man/man3/Esys_ClockRateAdjust.3
/usr/share/man/man3/Esys_ClockSet.3
/usr/share/man/man3/Esys_Commit.3
/usr/share/man/man3/Esys_ContextLoad.3
/usr/share/man/man3/Esys_ContextSave.3
/usr/share/man/man3/Esys_Create.3
/usr/share/man/man3/Esys_CreatePrimary.3
/usr/share/man/man3/Esys_DictionaryAttackLockReset.3
/usr/share/man/man3/Esys_DictionaryAttackParameters.3
/usr/share/man/man3/Esys_Duplicate.3
/usr/share/man/man3/Esys_ECC_Parameters.3
/usr/share/man/man3/Esys_ECDH_KeyGen.3
/usr/share/man/man3/Esys_ECDH_ZGen.3
/usr/share/man/man3/Esys_EC_Ephemeral.3
/usr/share/man/man3/Esys_EncryptDecrypt.3
/usr/share/man/man3/Esys_EventSequenceComplete.3
/usr/share/man/man3/Esys_EvictControl.3
/usr/share/man/man3/Esys_FlushContext.3
/usr/share/man/man3/Esys_GetCapability.3
/usr/share/man/man3/Esys_GetCommandAuditDigest.3
/usr/share/man/man3/Esys_GetRandom.3
/usr/share/man/man3/Esys_GetSessionAuditDigest.3
/usr/share/man/man3/Esys_GetTestResult.3
/usr/share/man/man3/Esys_GetTime.3
/usr/share/man/man3/Esys_HMAC.3
/usr/share/man/man3/Esys_HMAC_Start.3
/usr/share/man/man3/Esys_Hash.3
/usr/share/man/man3/Esys_HashSequenceStart.3
/usr/share/man/man3/Esys_HierarchyChangeAuth.3
/usr/share/man/man3/Esys_HierarchyControl.3
/usr/share/man/man3/Esys_Import.3
/usr/share/man/man3/Esys_IncrementalSelfTest.3
/usr/share/man/man3/Esys_Load.3
/usr/share/man/man3/Esys_LoadExternal.3
/usr/share/man/man3/Esys_MakeCredential.3
/usr/share/man/man3/Esys_NV_Certify.3
/usr/share/man/man3/Esys_NV_ChangeAuth.3
/usr/share/man/man3/Esys_NV_DefineSpace.3
/usr/share/man/man3/Esys_NV_Extend.3
/usr/share/man/man3/Esys_NV_GlobalWriteLock.3
/usr/share/man/man3/Esys_NV_Increment.3
/usr/share/man/man3/Esys_NV_Read.3
/usr/share/man/man3/Esys_NV_ReadLock.3
/usr/share/man/man3/Esys_NV_ReadPublic.3
/usr/share/man/man3/Esys_NV_SetBits.3
/usr/share/man/man3/Esys_NV_UndefineSpace.3
/usr/share/man/man3/Esys_NV_UndefineSpaceSpecial.3
/usr/share/man/man3/Esys_NV_Write.3
/usr/share/man/man3/Esys_NV_WriteLock.3
/usr/share/man/man3/Esys_ObjectChangeAuth.3
/usr/share/man/man3/Esys_PCR_Allocate.3
/usr/share/man/man3/Esys_PCR_Event.3
/usr/share/man/man3/Esys_PCR_Extend.3
/usr/share/man/man3/Esys_PCR_Read.3
/usr/share/man/man3/Esys_PCR_Reset.3
/usr/share/man/man3/Esys_PCR_SetAuthPolicy.3
/usr/share/man/man3/Esys_PCR_SetAuthValue.3
/usr/share/man/man3/Esys_PP_Commands.3
/usr/share/man/man3/Esys_PolicyAuthValue.3
/usr/share/man/man3/Esys_PolicyAuthorize.3
/usr/share/man/man3/Esys_PolicyCommandCode.3
/usr/share/man/man3/Esys_PolicyCounterTimer.3
/usr/share/man/man3/Esys_PolicyCpHash.3
/usr/share/man/man3/Esys_PolicyDuplicationSelect.3
/usr/share/man/man3/Esys_PolicyGetDigest.3
/usr/share/man/man3/Esys_PolicyLocality.3
/usr/share/man/man3/Esys_PolicyNV.3
/usr/share/man/man3/Esys_PolicyNameHash.3
/usr/share/man/man3/Esys_PolicyNvWritten.3
/usr/share/man/man3/Esys_PolicyOR.3
/usr/share/man/man3/Esys_PolicyPCR.3
/usr/share/man/man3/Esys_PolicyPassword.3
/usr/share/man/man3/Esys_PolicyPhysicalPresence.3
/usr/share/man/man3/Esys_PolicyRestart.3
/usr/share/man/man3/Esys_PolicySecret.3
/usr/share/man/man3/Esys_PolicySigned.3
/usr/share/man/man3/Esys_PolicyTicket.3
/usr/share/man/man3/Esys_Quote.3
/usr/share/man/man3/Esys_RSA_Decrypt.3
/usr/share/man/man3/Esys_RSA_Encrypt.3
/usr/share/man/man3/Esys_ReadClock.3
/usr/share/man/man3/Esys_ReadPublic.3
/usr/share/man/man3/Esys_Rewrap.3
/usr/share/man/man3/Esys_SelfTest.3
/usr/share/man/man3/Esys_SequenceComplete.3
/usr/share/man/man3/Esys_SequenceUpdate.3
/usr/share/man/man3/Esys_SetAlgorithmSet.3
/usr/share/man/man3/Esys_SetCommandCodeAuditStatus.3
/usr/share/man/man3/Esys_SetPrimaryPolicy.3
/usr/share/man/man3/Esys_Shutdown.3
/usr/share/man/man3/Esys_Sign.3
/usr/share/man/man3/Esys_StartAuthSession.3
/usr/share/man/man3/Esys_Startup.3
/usr/share/man/man3/Esys_StirRandom.3
/usr/share/man/man3/Esys_TestParms.3
/usr/share/man/man3/Esys_Unseal.3
/usr/share/man/man3/Esys_Vendor_TCG_Test.3
/usr/share/man/man3/Esys_VerifySignature.3
/usr/share/man/man3/Esys_ZGen_2Phase.3
/usr/share/man/man3/FapiTestgroup.3
/usr/share/man/man3/Fapi_AuthorizePolicy.3
/usr/share/man/man3/Fapi_ChangeAuth.3
/usr/share/man/man3/Fapi_CreateKey.3
/usr/share/man/man3/Fapi_CreateNv.3
/usr/share/man/man3/Fapi_CreateSeal.3
/usr/share/man/man3/Fapi_Decrypt.3
/usr/share/man/man3/Fapi_Delete.3
/usr/share/man/man3/Fapi_Encrypt.3
/usr/share/man/man3/Fapi_ExportKey.3
/usr/share/man/man3/Fapi_ExportPolicy.3
/usr/share/man/man3/Fapi_Finalize.3
/usr/share/man/man3/Fapi_Free.3
/usr/share/man/man3/Fapi_GetAppData.3
/usr/share/man/man3/Fapi_GetCertificate.3
/usr/share/man/man3/Fapi_GetDescription.3
/usr/share/man/man3/Fapi_GetInfo.3
/usr/share/man/man3/Fapi_GetPlatformCertificates.3
/usr/share/man/man3/Fapi_GetPollHandles.3
/usr/share/man/man3/Fapi_GetRandom.3
/usr/share/man/man3/Fapi_GetTcti.3
/usr/share/man/man3/Fapi_GetTpmBlobs.3
/usr/share/man/man3/Fapi_Import.3
/usr/share/man/man3/Fapi_Initialize.3
/usr/share/man/man3/Fapi_List.3
/usr/share/man/man3/Fapi_NvExtend.3
/usr/share/man/man3/Fapi_NvIncrement.3
/usr/share/man/man3/Fapi_NvRead.3
/usr/share/man/man3/Fapi_NvSetBits.3
/usr/share/man/man3/Fapi_NvWrite.3
/usr/share/man/man3/Fapi_PcrExtend.3
/usr/share/man/man3/Fapi_PcrRead.3
/usr/share/man/man3/Fapi_Provision.3
/usr/share/man/man3/Fapi_Quote.3
/usr/share/man/man3/Fapi_SetAppData.3
/usr/share/man/man3/Fapi_SetAuthCB.3
/usr/share/man/man3/Fapi_SetBranchCB.3
/usr/share/man/man3/Fapi_SetCertificate.3
/usr/share/man/man3/Fapi_SetDescription.3
/usr/share/man/man3/Fapi_SetSignCB.3
/usr/share/man/man3/Fapi_Sign.3
/usr/share/man/man3/Fapi_Unseal.3
/usr/share/man/man3/Fapi_VerifyQuote.3
/usr/share/man/man3/Fapi_VerifySignature.3
/usr/share/man/man3/Fapi_WriteAuthorizeNv.3
/usr/share/man/man3/Tss2_TctiLdr_Finalize.3
/usr/share/man/man3/Tss2_TctiLdr_FreeInfo.3
/usr/share/man/man3/Tss2_TctiLdr_GetInfo.3
/usr/share/man/man3/Tss2_TctiLdr_Initialize.3
/usr/share/man/man3/Tss2_Tcti_Cmd_Init.3
/usr/share/man/man3/Tss2_Tcti_Device_Init.3
/usr/share/man/man3/Tss2_Tcti_Mssim_Init.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtss2-esys.so.0
/usr/lib64/libtss2-esys.so.0.0.0
/usr/lib64/libtss2-fapi.so.1
/usr/lib64/libtss2-fapi.so.1.0.0
/usr/lib64/libtss2-mu.so.0
/usr/lib64/libtss2-mu.so.0.0.0
/usr/lib64/libtss2-rc.so.0
/usr/lib64/libtss2-rc.so.0.0.0
/usr/lib64/libtss2-sys.so.1
/usr/lib64/libtss2-sys.so.1.0.0
/usr/lib64/libtss2-tcti-cmd.so.0
/usr/lib64/libtss2-tcti-cmd.so.0.0.0
/usr/lib64/libtss2-tcti-device.so.0
/usr/lib64/libtss2-tcti-device.so.0.0.0
/usr/lib64/libtss2-tcti-mssim.so.0
/usr/lib64/libtss2-tcti-mssim.so.0.0.0
/usr/lib64/libtss2-tcti-pcap.so.0
/usr/lib64/libtss2-tcti-pcap.so.0.0.0
/usr/lib64/libtss2-tcti-swtpm.so.0
/usr/lib64/libtss2-tcti-swtpm.so.0.0.0
/usr/lib64/libtss2-tctildr.so.0
/usr/lib64/libtss2-tctildr.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tpm2-tss/af62924ad3089277c413ea767486f404ac159ce1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/fapi-config.5
/usr/share/man/man5/fapi-profile.5
/usr/share/man/man7/tss2-tcti-cmd.7
/usr/share/man/man7/tss2-tcti-device.7
/usr/share/man/man7/tss2-tcti-mssim.7
/usr/share/man/man7/tss2-tcti-swtpm.7
/usr/share/man/man7/tss2-tctildr.7

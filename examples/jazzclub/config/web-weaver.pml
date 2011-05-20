<?xml version="1.0"?>
<!-- 
 !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 !
 !                                DANSE/vnf team
 !                       California Institute of Technology
 !                       (C) 2008-2009  All Rights Reserved
 !
 !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

    <component name="web-weaver">

        <!-- transformation configuration -->
	<property name="controller-url">/cgi-bin/main.py</property>
	<property name="html-base">http://localhost:8100/</property>
	<property name="cookie-path">/cgi-bin/</property>
	<property name="use-cookie">on</property>

        <!-- user info -->
        <property name="author">DANSE vnf team</property>
        <property name="organization">California Institute of Technology</property>
        <property name="copyright">2008-2009</property>
        <property name="creator">luban</property>

        <!-- banner -->
        <property name="bannerWidth">78</property>
        <property name="bannerCharacter">~</property>
        <property name="timestamp">no</property>

        <!-- license -->
        <property name="licenseText">{LicenseText}</property>
    </component>

</inventory>

<!-- $Id$ -->

<!-- End of file -->

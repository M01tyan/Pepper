<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Pepper_2" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="__init__" src="lib/paho/__init__.py" />
        <File name="__init__" src="lib/paho/mqtt/__init__.py" />
        <File name="client" src="lib/paho/mqtt/client.py" />
        <File name="matcher" src="lib/paho/mqtt/matcher.py" />
        <File name="publish" src="lib/paho/mqtt/publish.py" />
        <File name="subscribe" src="lib/paho/mqtt/subscribe.py" />
    </Resources>
    <Topics />
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>

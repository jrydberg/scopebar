# Copyright (C) 2009 Johan Rydberg <johan.rydberg@gmail.com>

import objc
from Foundation import *

objc.loadBundle(
    "ScopeBar", globals(), 
    bundle_path=objc.pathForFramework("/System/Library/Frameworks/ScopeBar.framework")
    #bundle_identifier="com.mattgemmell.ScopeBar",
    #bundle_path="/System/Library/Frameworks/ScopeBar.framework"
    )


MGScopeBarDataSource = objc.informal_protocol(
    "MGScopeBarDataSource",
    [
        objc.selector(
            None,
            selector="numberOfGroupsInScopeBar:",
            signature="i@:@",
            isRequired=1,
            ),
        objc.selector(
            None,
            selector="scopeBar:itemIdentifiersForGroup:",
            signature="@@:@i",
            isRequired=1,
            ),
        objc.selector(
            None,
            selector="scopeBar:labelForGroup:",
            signature="@@:@i",
            isRequired=1,
            ),
        objc.selector(
            None,
            selector="scopeBar:selectionModeForGroup:",
            signature="i@:@i",
            isRequired=1,
            ),
        objc.selector(
            None,
            selector="scopeBar:titleOfItem:inGroup:",
            signature="@@:@@i",
            isRequired=1,
            ),
        
        objc.selector(
            None,
            selector="scopeBar:showSeparatorBeforeGroup:",
            signature="B@:@i",
            isRequired=0,
            ),
        
        objc.selector(
            None,
            selector="scopeBar:imageForItem:inGroup:",
            signature="@@:@@i",
            isRequired=0,
            ),
        
        objc.selector(
            None,
            selector="accessoryViewForScopeBar:",
            signature="@:@",
            isRequired=0,
            ),
        ]
)

MGScopeBarDelegate = objc.informal_protocol(
    "MGScopeBarDelegate",
    [
        objc.selector(
            None,
            selector="scopeBar:selectedStateChanged:forItem:inGroup:",
            signature="@@:@B@i",
            isRequired=0,
            ),
        ]
    )

MGRadioSelectionMode = 0
MGMultipleSelectionMode = 1


class MGScopeBarController(NSObject):
    """
    Controller for MGScopeBars.
    """

    def numberOfGroupsInScopeBar_(self, view):
        return 0

    def scopeBar_itemIdentifiersForGroup_(self, view, index):
        return []
    
    def scopeBar_labelForGroup_(self, view, identifier):
        return None
    
    def scopeBar_selectionModeForGroup_(self, view, index):
        return MGRadioSelectionMode

    def scopeBar_titleOfItem_inGroup_(self, view, identifier, index):
        return identifier.upper()

#
#  ScopeBarExampleAppDelegate.py
#  ScopeBarExample
#
#  Created by Johan Rydberg on 4/23/09.
#  Copyright __MyCompanyName__ 2009. All rights reserved.
#

from Foundation import *
from AppKit import *
from MGScopeBar import *

class ScopeBarExampleAppDelegate(NSObject):
    label = objc.IBOutlet()
    accessory = objc.IBOutlet()
    scopeBar = objc.IBOutlet()
    
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
        self.scopeBar.reloadData()
        
    def accessoryViewForScopeBar_(self, view):
        return self.accessory
    
    def numberOfGroupsInScopeBar_(self, view):
        """
        Return the number of groups in the scope bar.
        """
        return 3

    def scopeBar_itemIdentifiersForGroup_(self, view, groupIndex):
        """
        Return item identifiers for the specified group.
        """
        if groupIndex == 0:
            return ["HereItem", "ThereItem"]
        elif groupIndex == 1:
            return ["ContentsItem", "FileNamesItem", "MetadataItem"]
        else:
            return ["AllFilesItem", "ImagesOnlyItem"]
    
    def scopeBar_labelForGroup_(self, view, groupIndex):
        """
        Return label for the group.  
        """
        if groupIndex == 0:
            return "Search:"
        elif groupIndex == 1:
            return None
        else:
            return "Kind:"
    
    def scopeBar_selectionModeForGroup_(self, view, groupIndex):
        """
        Return selection mode for group.
        """
        if groupIndex == 0:
            return MGRadioSelectionMode
        elif groupIndex == 1:
            return MGMultipleSelectionMode
        else:
            return MGRadioSelectionMode

    def scopeBar_titleOfItem_inGroup_(self, view, identifier, groupIndex):
        """
        Return title of item.
        """
        return identifier[:-4]

    def scopeBar_showSeparatorBeforeGroup_(self, view, groupIndex):
        """
        Return whether a separator should be rendered before given group.
        """
        return (groupIndex != 0)

    def scopeBar_imageForItem_inGroup_(self, view, identifier, groupIndex):
        """
        Return possible C{NSImage} to display before item.
        
        @rtype: a NSImage.
        """
        if groupIndex == 0:
            return NSImage.imageNamed_("NSComputer")
        elif groupIndex == 2:
            if identifier == "AllFilesItem":
                return NSImage.imageNamed_("NSGenericDocument")
            else:
                return NSWorkspace.sharedWorkspace().iconForFileType_("png")
        return None

    def scopeBar_selectedStateChanged_forItem_inGroup_(self, view, selected, 
                                                       identifier, groupIndex):
        """
        Delegate method that is invoked when state is changed for an
        item.
        """
        displayString = "'%s' %s in group %d." % (
            self.scopeBar_titleOfItem_inGroup_(view, identifier, groupIndex),
            (selected and "selected" or "deseelcted"),
            groupIndex
            )
        self.label.setStringValue_(displayString)

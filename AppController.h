//
//  AppController.h
//  MGScopeBar
//
//  Created by Matt Gemmell on 16/03/2008.
//

#import <Cocoa/Cocoa.h>
#import "MGScopeBarDelegateProtocol.h"

@interface AppController : NSObject {
	IBOutlet NSTextField *labelField;
	IBOutlet MGScopeBar *scopeBar;
	IBOutlet NSView *accessoryView;
	NSMutableArray *groups;
}

// MGScopeBarDataSource:
- (int)numberOfGroupsInScopeBar:(MGScopeBar *)theScopeBar;
- (NSArray *)scopeBar:(MGScopeBar *)theScopeBar itemIdentifiersForGroup:(int)groupNumber;
- (NSString *)scopeBar:(MGScopeBar *)theScopeBar labelForGroup:(int)groupNumber; // return nil or an empty string for no label.
- (MGScopeBarGroupSelectionMode)scopeBar:(MGScopeBar *)theScopeBar selectionModeForGroup:(int)groupNumber;
- (NSString *)scopeBar:(MGScopeBar *)theScopeBar titleOfItem:(NSString *)identifier inGroup:(int)groupNumber;

// If the following method is not implemented, all groups except the first will have a separator before them.
- (BOOL)scopeBar:(MGScopeBar *)theScopeBar showSeparatorBeforeGroup:(int)groupNumber;
- (NSImage *)scopeBar:(MGScopeBar *)theScopeBar imageForItem:(NSString *)identifier inGroup:(int)groupNumber; // default is no image. Will be shown at 16x16.
- (NSView *)accessoryViewForScopeBar:(MGScopeBar *)theScopeBar; // default is no accessory view.

// MGScopeBarDelegate:
- (void)scopeBar:(MGScopeBar *)theScopeBar selectedStateChanged:(BOOL)selected forItem:(NSString *)identifier inGroup:(int)groupNumber;

@property(retain) NSMutableArray *groups;

@end

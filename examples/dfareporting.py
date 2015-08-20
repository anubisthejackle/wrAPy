from wrAPy.Apis.Google import DFAReporting
import sys

profileId = sys.argv[1]

print '########## ADVERTISERS FOR PROFILE ID ' + profileId + ' #########'
print DFAReporting().get('/userprofiles/' + profileId + '/advertisers')

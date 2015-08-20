from wrAPy.Apis.Google import DFAReporting
import sys

dfp = DFAReporting()
profileId = sys.argv[1]

result = dfp.get('/userprofiles/' + profileId + '/advertisers')

print '########## ADVERTISERS FOR PROFILE ID ' + profileId + ' #########'
print result

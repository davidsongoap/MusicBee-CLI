#----------------------------------------------------------#
#- MusicBeeIPCSDK Py v2.0.0                               -#
#- Copyright © Kerli Low 2014                             -#
#- This file is licensed under the                        -#
#- BSD 2-Clause License                                   -#
#- See LICENSE_MusicBeeIPCSDK for more information.       -#
#----------------------------------------------------------#

# MBBool
MB_False    = 0
MB_True     = 1

# MBError
MBE_Error                   = 0
MBE_NoError                 = 1
MBE_CommandNotRecognized    = 2

# MBPlayState
MBPS_Undefined  = 0
MBPS_Loading    = 1
MBPS_Playing    = 3
MBPS_Paused     = 6
MBPS_Stopped    = 7

# MBRepeatMode
MBRM_None   = 0
MBRM_All    = 1
MBRM_One    = 2
   
# MBReplayGainMode
MBRGM_Off   = 0
MBRGM_Track = 1
MBRGM_Album = 2
MBRGM_Smart = 3

# MBFileProperty
MBFP_Url                    = 2
MBFP_Kind                   = 4
MBFP_Format                 = 5
MBFP_Size                   = 7
MBFP_Channels               = 8
MBFP_SampleRate             = 9
MBFP_Bitrate                = 10
MBFP_DateModified           = 11
MBFP_DateAdded              = 12
MBFP_LastPlayed             = 13
MBFP_PlayCount              = 14
MBFP_SkipCount              = 15
MBFP_Duration               = 16
MBFP_NowPlayingListIndex    = 78  # only has meaning when called from NowPlayingList_* commands
MBFP_ReplayGainTrack        = 94
MBFP_ReplayGainAlbum        = 95

# MBMetaData
MBMD_TrackTitle     = 65
MBMD_Album          = 30
MBMD_AlbumArtist    = 31       # displayed album artist
MBMD_AlbumArtistRaw = 34       # stored album artist
MBMD_Artist         = 32       # displayed artist
MBMD_MultiArtist    = 33       # individual artists separated by a null char
MBMD_PrimaryArtist  = 19       # first artist from multi-artist tagged file otherwise displayed artist
MBMD_Artists                  = 144
MBMD_ArtistsWithArtistRole    = 145
MBMD_ArtistsWithPerformerRole = 146
MBMD_ArtistsWithGuestRole     = 147
MBMD_ArtistsWithRemixerRole   = 148
MBMD_Artwork        = 40
MBMD_BeatsPerMin    = 41
MBMD_Composer       = 43       # displayed composer
MBMD_MultiComposer  = 89       # individual composers separated by a null char
MBMD_Comment        = 44
MBMD_Conductor      = 45
MBMD_Custom1        = 46
MBMD_Custom2        = 47
MBMD_Custom3        = 48
MBMD_Custom4        = 49
MBMD_Custom5        = 50
MBMD_Custom6        = 96
MBMD_Custom7        = 97
MBMD_Custom8        = 98
MBMD_Custom9        = 99
MBMD_Custom10       = 128
MBMD_Custom11       = 129
MBMD_Custom12       = 130
MBMD_Custom13       = 131
MBMD_Custom14       = 132
MBMD_Custom15       = 133
MBMD_Custom16       = 134
MBMD_DiscNo         = 52
MBMD_DiscCount      = 54
MBMD_Encoder        = 55
MBMD_Genre          = 59
MBMD_Genres         = 103
MBMD_GenreCategory  = 60
MBMD_Grouping       = 61
MBMD_Keywords       = 84
MBMD_HasLyrics      = 63
MBMD_Lyricist       = 62
MBMD_Lyrics         = 114
MBMD_Mood           = 64
MBMD_Occasion       = 66
MBMD_Origin         = 67
MBMD_Publisher      = 73
MBMD_Quality        = 74
MBMD_Rating         = 75
MBMD_RatingLove     = 76
MBMD_RatingAlbum    = 104
MBMD_Tempo          = 85
MBMD_TrackNo        = 86
MBMD_TrackCount     = 87
MBMD_Virtual1       = 109
MBMD_Virtual2       = 110
MBMD_Virtual3       = 111
MBMD_Virtual4       = 112
MBMD_Virtual5       = 113
MBMD_Virtual6       = 122
MBMD_Virtual7       = 123
MBMD_Virtual8       = 124
MBMD_Virtual9       = 125
MBMD_Virtual10      = 135
MBMD_Virtual11      = 136
MBMD_Virtual12      = 137
MBMD_Virtual13      = 138
MBMD_Virtual14      = 139
MBMD_Virtual15      = 140
MBMD_Virtual16      = 141
MBMD_Year           = 88

# MBLibraryCategory
MBLC_Music       = 0
MBLC_Audiobook   = 1
MBLC_Video       = 2
MBLC_Inbox       = 4

# MBDataType
MBDT_String      = 0
MBDT_Number      = 1
MBDT_DateTime    = 2
MBDT_Rating      = 3

# MBLyricsType
MBLT_NotSpecified    = 0
MBLT_Synchronised    = 1
MBLT_UnSynchronised  = 2

# MBPlayButtonType
MBPBT_PreviousTrack   = 0
MBPBT_PlayPause       = 1
MBPBT_NextTrack       = 2
MBPBT_Stop            = 3

# MBPlaylistFormat
MBPF_Unknown     = 0
MBPF_M3u         = 1
MBPF_Xspf        = 2
MBPF_Asx         = 3
MBPF_Wpl         = 4
MBPF_Pls         = 5
MBPF_Auto        = 7
MBPF_M3uAscii    = 8
MBPF_AsxFile     = 9
MBPF_Radio       = 10
MBPF_M3uExtended = 11
MBPF_Mbp         = 12

# MBMusicBeeVersion
MBMBV_v2_0 = 0
MBMBV_v2_1 = 1
MBMBV_v2_2 = 2
MBMBV_v2_3 = 3

# MBCommand
MBC_PlayPause                           = 100      # WM_USER
MBC_Play                                = 101      # WM_USER
MBC_Pause                               = 102      # WM_USER
MBC_Stop                                = 103      # WM_USER
MBC_StopAfterCurrent                    = 104      # WM_USER
MBC_PreviousTrack                       = 105      # WM_USER
MBC_NextTrack                           = 106      # WM_USER
MBC_StartAutoDj                         = 107      # WM_USER
MBC_EndAutoDj                           = 108      # WM_USER
MBC_GetPlayState                        = 109      # WM_USER
MBC_GetPosition                         = 110      # WM_USER
MBC_SetPosition                         = 111      # WM_USER
MBC_GetVolume                           = 112      # WM_USER
MBC_SetVolume                           = 113      # WM_USER
MBC_GetVolumep                          = 114      # WM_USER
MBC_SetVolumep                          = 115      # WM_USER
MBC_GetVolumef                          = 116      # WM_USER
MBC_SetVolumef                          = 117      # WM_USER
MBC_GetMute                             = 118      # WM_USER
MBC_SetMute                             = 119      # WM_USER
MBC_GetShuffle                          = 120      # WM_USER
MBC_SetShuffle                          = 121      # WM_USER
MBC_GetRepeat                           = 122      # WM_USER
MBC_SetRepeat                           = 123      # WM_USER
MBC_GetEqualiserEnabled                 = 124      # WM_USER
MBC_SetEqualiserEnabled                 = 125      # WM_USER
MBC_GetDspEnabled                       = 126      # WM_USER
MBC_SetDspEnabled                       = 127      # WM_USER
MBC_GetScrobbleEnabled                  = 128      # WM_USER
MBC_SetScrobbleEnabled                  = 129      # WM_USER
MBC_ShowEqualiser                       = 130      # WM_USER
MBC_GetAutoDjEnabled                    = 131      # WM_USER
MBC_GetStopAfterCurrentEnabled          = 132      # WM_USER
MBC_SetStopAfterCurrentEnabled          = 133      # WM_USER
MBC_GetCrossfade                        = 134      # WM_USER
MBC_SetCrossfade                        = 135      # WM_USER
MBC_GetReplayGainMode                   = 136      # WM_USER
MBC_SetReplayGainMode                   = 137      # WM_USER
MBC_QueueRandomTracks                   = 138      # WM_USER
MBC_GetDuration                         = 139      # WM_USER
MBC_GetFileUrl                          = 140      # WM_USER
MBC_GetFileProperty                     = 141      # WM_USER
MBC_GetFileTag                          = 142      # WM_USER
MBC_GetLyrics                           = 143      # WM_USER
MBC_GetDownloadedLyrics                 = 144      # WM_USER
MBC_GetArtwork                          = 145      # WM_USER
MBC_GetArtworkUrl                       = 146      # WM_USER
MBC_GetDownloadedArtwork                = 147      # WM_USER
MBC_GetDownloadedArtworkUrl             = 148      # WM_USER
MBC_GetArtistPicture                    = 149      # WM_USER
MBC_GetArtistPictureUrls                = 150      # WM_USER
MBC_GetArtistPictureThumb               = 151      # WM_USER
MBC_IsSoundtrack                        = 152      # WM_USER
MBC_GetSoundtrackPictureUrls            = 153      # WM_USER
MBC_GetCurrentIndex                     = 154      # WM_USER
MBC_GetNextIndex                        = 155      # WM_USER
MBC_IsAnyPriorTracks                    = 156      # WM_USER
MBC_IsAnyFollowingTracks                = 157      # WM_USER
MBC_PlayNow                             = 158      # WM_COPYDATA
MBC_QueueNext                           = 159      # WM_COPYDATA
MBC_QueueLast                           = 160      # WM_COPYDATA
MBC_RemoveAt                            = 161      # WM_USER
MBC_ClearNowPlayingList                 = 162      # WM_USER
MBC_MoveFiles                           = 163      # WM_COPYDATA
MBC_ShowNowPlayingAssistant             = 164      # WM_USER
MBC_GetShowTimeRemaining                = 165      # WM_USER
MBC_GetShowRatingTrack                  = 166      # WM_USER
MBC_GetShowRatingLove                   = 167      # WM_USER
MBC_GetButtonEnabled                    = 168      # WM_USER
MBC_Jump                                = 169      # WM_USER
MBC_Search                              = 170      # WM_COPYDATA
MBC_SearchFirst                         = 171      # WM_COPYDATA
MBC_SearchIndices                       = 172      # WM_COPYDATA
MBC_SearchFirstIndex                    = 173      # WM_COPYDATA
MBC_SearchAndPlayFirst                  = 174      # WM_COPYDATA
MBC_NowPlayingList_GetListFileUrl       = 200      # WM_COPYDATA
MBC_NowPlayingList_GetFileProperty      = 201      # WM_COPYDATA
MBC_NowPlayingList_GetFileTag           = 202      # WM_COPYDATA
MBC_NowPlayingList_QueryFiles           = 203      # WM_COPYDATA
MBC_NowPlayingList_QueryGetNextFile     = 204      # WM_USER
MBC_NowPlayingList_QueryGetAllFiles     = 205      # WM_USER
MBC_NowPlayingList_QueryFilesEx         = 206      # WM_COPYDATA
MBC_NowPlayingList_PlayLibraryShuffled  = 207      # WM_USER
MBC_NowPlayingList_GetItemCount         = 208      # WM_USER
MBC_Playlist_GetName                    = 300      # WM_COPYDATA
MBC_Playlist_GetType                    = 301      # WM_COPYDATA
MBC_Playlist_IsInList                   = 302      # WM_COPYDATA
MBC_Playlist_QueryPlaylists             = 303      # WM_USER
MBC_Playlist_QueryGetNextPlaylist       = 304      # WM_USER
MBC_Playlist_QueryFiles                 = 305      # WM_COPYDATA
MBC_Playlist_QueryGetNextFile           = 306      # WM_USER
MBC_Playlist_QueryGetAllFiles           = 307      # WM_USER
MBC_Playlist_QueryFilesEx               = 308      # WM_COPYDATA
MBC_Playlist_CreatePlaylist             = 309      # WM_COPYDATA
MBC_Playlist_DeletePlaylist             = 310      # WM_COPYDATA
MBC_Playlist_SetFiles                   = 311      # WM_COPYDATA
MBC_Playlist_AppendFiles                = 312      # WM_COPYDATA
MBC_Playlist_RemoveAt                   = 313      # WM_COPYDATA
MBC_Playlist_MoveFiles                  = 314      # WM_COPYDATA
MBC_Playlist_PlayNow                    = 315      # WM_COPYDATA
MBC_Playlist_GetItemCount               = 316      # WM_COPYDATA
MBC_Library_GetFileProperty             = 400      # WM_COPYDATA
MBC_Library_GetFileTag                  = 401      # WM_COPYDATA
MBC_Library_SetFileTag                  = 402      # WM_COPYDATA
MBC_Library_CommitTagsToFile            = 403      # WM_COPYDATA
MBC_Library_GetLyrics                   = 404      # WM_COPYDATA
MBC_Library_GetArtwork                  = 405      # WM_COPYDATA
MBC_Library_GetArtworkUrl               = 406      # WM_COPYDATA
MBC_Library_GetArtistPicture            = 407      # WM_COPYDATA
MBC_Library_GetArtistPictureUrls        = 408      # WM_COPYDATA
MBC_Library_GetArtistPictureThumb       = 409      # WM_COPYDATA
MBC_Library_AddFileToLibrary            = 410      # WM_COPYDATA
MBC_Library_QueryFiles                  = 411      # WM_COPYDATA
MBC_Library_QueryGetNextFile            = 412      # WM_USER
MBC_Library_QueryGetAllFiles            = 413      # WM_USER
MBC_Library_QueryFilesEx                = 414      # WM_COPYDATA
MBC_Library_QuerySimilarArtists         = 415      # WM_COPYDATA
MBC_Library_QueryLookupTable            = 416      # WM_COPYDATA
MBC_Library_QueryGetLookupTableValue    = 417      # WM_COPYDATA
MBC_Library_GetItemCount                = 418      # WM_USER
MBC_Library_Jump                        = 419      # WM_USER
MBC_Library_Search                      = 420      # WM_COPYDATA
MBC_Library_SearchFirst                 = 421      # WM_COPYDATA
MBC_Library_SearchIndices               = 422      # WM_COPYDATA
MBC_Library_SearchFirstIndex            = 423      # WM_COPYDATA
MBC_Library_SearchAndPlayFirst          = 424      # WM_COPYDATA
MBC_Setting_GetFieldName                = 700      # WM_COPYDATA
MBC_Setting_GetDataType                 = 701      # WM_COPYDATA
MBC_Window_GetHandle                    = 800      # WM_USER
MBC_Window_Close                        = 801      # WM_USER
MBC_Window_Restore                      = 802      # WM_USER
MBC_Window_Minimize                     = 803      # WM_USER
MBC_Window_Maximize                     = 804      # WM_USER
MBC_Window_Move                         = 805      # WM_USER
MBC_Window_Resize                       = 806      # WM_USER
MBC_Window_BringToFront                 = 807      # WM_USER
MBC_Window_GetPosition                  = 808      # WM_USER
MBC_Window_GetSize                      = 809      # WM_USER
MBC_FreeLRESULT                         = 900      # WM_USER
MBC_MusicBeeVersion                     = 995      # WM_USER
MBC_PluginVersion                       = 996      # WM_USER
MBC_Test                                = 997      # WM_USER      For debugging purposes
MBC_MessageBox                          = 998      # WM_COPYDATA  For debugging purposes
MBC_Probe                               = 999      # WM_USER      To test MusicBeeIPC hwnd is valid

# Window Message
WM_USER     = 0x0400
WM_COPYDATA = 0x004A

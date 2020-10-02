# ----------------------------------------------------------#
# - MusicBeeIPCSDK Py v2.0.0                               -#
# - Copyright © Kerli Low 2014                             -#
# - This file is licensed under the                        -#
# - BSD 2-Clause License                                   -#
# - See LICENSE_MusicBeeIPCSDK for more information.       -#
# ----------------------------------------------------------#

import array
from win32api import SendMessage
from win32gui import FindWindow
from ctypes import *
from .enums import *
from .structs import *
from .pack import *
from .unpack import *


class MusicBeeIPC:
    def probe(self):
        """
        :rtype: bool
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Probe, 0) != MBE_Error

    def play_pause(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_PlayPause, 0)

    def play(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Play, 0)

    def pause(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Pause, 0)

    def stop(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Stop, 0)

    def stop_after_current(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_StopAfterCurrent, 0)

    def previous_track(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_PreviousTrack, 0)

    def next_track(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_NextTrack, 0)

    def start_auto_dj(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_StartAutoDj, 0)

    def end_auto_dj(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_EndAutoDj, 0)

    def get_play_state(self):
        """
        :rtype: MBPlayState
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetPlayState, 0)

    def get_play_state_str(self):
        """
        :rtype: str
        """
        play_state = SendMessage(self.find_hwnd(), WM_USER, MBC_GetPlayState, 0)
        if play_state == MBPS_Loading:
            return "Loading"
        elif play_state == MBPS_Playing:
            return "Playing"
        elif play_state == MBPS_Paused:
            return "Paused"
        elif play_state == MBPS_Stopped:
            return "Stopped"
        else:
            return "Undefined"

    def get_position(self):
        """
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetPosition, 0)

    def set_position(self, position):
        """
        :param position:
        :type position: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetPosition, position)

    @property
    def position(self):
        """
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetPosition, 0)

    @position.setter
    def position(self, position):
        """
        :param position:
        :type position: int
        """
        SendMessage(self.find_hwnd(), WM_USER, MBC_SetPosition, position)

    def get_volume(self):
        """
        Volume: Value between 0 - 100
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetVolume, 0)

    def set_volume(self, volume):
        """
        Volume: Value between 0 - 100
        :param volume:
        :type volume: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetVolume, volume)

    @property
    def volume(self):
        """
        Volume: Value between 0 - 100
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetVolume, 0)

    @volume.setter
    def volume(self, volume):
        """
        Volume: Value between 0 - 100
        :param volume:
        :type volume: int
        """
        SendMessage(self.find_hwnd(), WM_USER, MBC_SetVolume, volume)

    def get_volumep(self):
        """
        Precise volume: Value between 0 - 10000
        :rtyp e: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetVolumep, 0)

    def set_volumep(self, volume):
        """
        Precise volume: Value between 0 - 10000
        :param volume:
        :type volume: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetVolumep, volume)

    @property
    def volumep(self):
        """
        Precise volume: Value between 0 - 10000
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetVolumep, 0)

    @volumep.setter
    def volumep(self, volume):
        """
        Precise volume: Value between 0 - 10000
        :param volume:
        :type volume: int
        """
        SendMessage(self.find_hwnd(), WM_USER, MBC_SetVolumep, volume)

    def get_volumef(self):
        """
        Floating point volume: Value between 0.0 - 1.0
        :rtype: float
        """
        return FloatInt(i=SendMessage(self.find_hwnd(), WM_USER, MBC_GetVolumef, 0)).f

    def set_volumef(self, volume):
        """
        Floating point volume: Value between 0.0 - 1.0
        :param volume:
        :type volume: float
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetVolumef, FloatInt(f=volume).i)

    @property
    def volumef(self):
        """
        Floating point volume: Value between 0.0 - 1.0
        :rtype: float
        """
        return FloatInt(i=SendMessage(self.find_hwnd(), WM_USER, MBC_GetVolumef, 0)).f

    @volumef.setter
    def volumef(self, volume):
        """
        Floating point volume: Value between 0.0 - 1.0
        :param volume:
        :type volume: float
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetVolumef, FloatInt(f=volume).i)

    def get_mute(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetMute, 0))

    def set_mute(self, mute):
        """
        :param mute:
        :type mute: bool
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetMute, int(mute))

    def get_shuffle(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetShuffle, 0))

    def set_shuffle(self, shuffle):
        """
        :param shuffle:
        :type shuffle: bool
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetShuffle, int(shuffle))

    def get_repeat(self):
        """
        :rtype: MBRepeatMode
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetRepeat, 0)

    def set_repeat(self, repeat):
        """
        :param repeat:
        :type repeat: MBRepeatMode
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetRepeat, repeat)

    def get_equalizer_enabled(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetEqualizerEnabled, 0))

    def set_equalizer_enabled(self, enabled):
        """
        :param enabled:
        :type enabled: bool
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetEqualizerEnabled, int(enabled))

    def get_dsp_enabled(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetDspEnabled, 0))

    def set_dsp_enabled(self, enabled):
        """
        :param enabled:
        :type enabled: bool
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetDspEnabled, int(enabled))

    def get_scrobble_enabled(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetScrobbleEnabled, 0))

    def set_scrobble_enabled(self, enabled):
        """
        :param enabled:
        :type enabled: bool
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetScrobbleEnabled, int(enabled))

    def show_equalizer(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_ShowEqualiser, 0)

    def get_auto_dj_enabled(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetAutoDjEnabled, 0))

    def get_stop_after_current_enabled(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetStopAfterCurrentEnabled, 0))

    def set_stop_after_current_enabled(self, enabled):
        """
        :param enabled:
        :type enabled: bool
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetStopAfterCurrentEnabled, int(enabled))

    def get_crossfade(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetCrossfade, 0))

    def set_crossfade(self, crossfade):
        """
        :param crossfade:
        :type crossfade: bool
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetCrossfade, int(crossfade))

    def get_replay_gain_mode(self):
        """
        :rtype: MBReplayGainMode
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetReplayGainMode, 0)

    def set_replay_gain_mode(self, mode):
        """
        :param mode:
        :type mode: MBReplayGainMode
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_SetReplayGainMode, mode)

    def queue_random_tracks(self, count):
        """
        :param count:
        :type count: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_QueueRandomTracks, count)

    def get_duration(self):
        """
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetDuration, 0)

    def get_file_url(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetFileUrl, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_file_property(self, file_property):
        """
        :param file_property:
        :type file_property: MBFileProperty
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetFileProperty, file_property)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_file_tag(self, field):
        """
        :param field:
        :type field: MBMetaData
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetFileTag, field)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_lyrics(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetLyrics, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_downloaded_lyrics(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetDownloadedLyrics, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_artwork(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetArtwork, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_artwork_url(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetArtworkUrl, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_downloaded_artwork(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetDownloadedArtwork, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_downloaded_artwork_url(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetDownloadedArtworkUrl, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_artist_picture(self, fading_percent):
        """
        :param fading_percent:
        :type fading_percent: int
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetArtistPicture, fading_percent)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_artist_picture_urls(self, local_only):
        """
        :param local_only:
        :type local_only: bool
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetArtistPictureUrls, int(local_only))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_artist_picture_thumb(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetArtistPictureThumb, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def is_soundtrack(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_IsSoundtrack, 0))

    def get_soundtrack_picture_urls(self, local_only):
        """
        :param local_only:
        :type local_only: bool
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_GetSoundtrackPictureUrls, int(local_only))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_current_index(self):
        """
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetCurrentIndex, 0)

    def get_next_index(self, offset):
        """
        :param offset:
        :type offset: int
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_GetNextIndex, offset)

    def is_any_prior_tracks(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_IsAnyPriorTracks, 0))

    def is_any_following_tracks(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_IsAnyFollowingTracks, 0))

    def play_now(self, fileurl):
        """
        :param fileurl:
        :type fileurl: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_PlayNow, pack_s(fileurl))

    def play_now_list(self, fileslist):
        """
        :param fileurl:
        :type fileurl: str
        :rtype: MBError
        """
        for fileurl in fileslist:
            self.queue_next(fileurl)

    def queue_next(self, fileurl):
        """
        :param fileurl:
        :type fileurl: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_QueueNext, pack_s(fileurl))

    def queue_last(self, fileurl):
        """
        :param fileurl:
        :type fileurl: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_QueueLast, pack_s(fileurl))

    def clear_now_playing_list(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_ClearNowPlayingList, 0)

    def remove_at(self, index):
        """
        :param index:
        :type index: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_RemoveAt, index)

    def move_files(self, from_indices, to_index):
        """
        :param from_indices:
        :type from_indices: list of int
        :param to_index:
        :type to_index: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_MoveFiles, pack_iai(from_indices, to_index))

    def show_now_playing_assistant(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_ShowNowPlayingAssistant, 0)

    def get_show_time_remaining(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetShowTimeRemaining, 0))

    def get_show_rating_track(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetShowRatingTrack, 0))

    def get_show_rating_love(self):
        """
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetShowRatingLove, 0))

    def get_button_enabled(self, button):
        """
        :param button:
        :type button: MBPlayButtonType
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_USER, MBC_GetButtonEnabled, button))

    def jump(self, index):
        """
        :param index:
        :type index: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Jump, index)

    def search(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Search, pack_sssa(query, comparison, fields))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def search_first(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_SearchFirst, pack_sssa(query, comparison, fields))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def search_indices(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: list of int
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_SearchIndices, pack_sssa(query, comparison, fields))

        r = unpack_ia(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def search_first_index(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_SearchFirstIndex, pack_sssa(query, comparison, fields))

    def search_and_play_first(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_SearchAndPlayFirst, pack_sssa(query, comparison, fields))

    def now_playing_list_get_list_file_url(self, index):
        """
        :param index:
        :type index: int
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_NowPlayingList_GetListFileUrl, index)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def now_playing_list_get_file_property(self, index, file_property):
        """
        :param index:
        :type index: int
        :param file_property:
        :type file_property: MBFileProperty
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_NowPlayingList_GetFileProperty, pack_i(index, file_property))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def now_playing_list_get_file_tag(self, index, field):
        """
        :param index:
        :type index: int
        :param field:
        :type field: MBMetaData
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_NowPlayingList_GetFileTag, pack_i(index, field))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def now_playing_list_query_files(self, query):
        """
        :param query:
        :type query: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_NowPlayingList_QueryFiles, pack_s(query))

    def now_playing_list_query_get_next_file(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_NowPlayingList_QueryGetNextFile, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def now_playing_list_query_get_all_files(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_NowPlayingList_QueryGetAllFiles, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def now_playing_list_query_files_ex(self, query):
        """
        :param query:
        :type query: str
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_NowPlayingList_QueryFilesEx, pack_s(query))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def now_playing_list_play_library_shuffled(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_NowPlayingList_PlayLibraryShuffled, 0)

    def now_playing_list_get_item_count(self):
        """
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_NowPlayingList_GetItemCount, 0)

    def playlist_get_name(self, playlist_url):
        """
        :param playlist_url:
        :type playlist_url: str
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Playlist_GetName, pack_s(playlist_url))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def playlist_get_type(self, playlist_url):
        """
        :param playlist_url:
        :type playlist_url: str
        :rtype: MBPlaylistFormat
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_GetType, pack_s(playlist_url))

    def playlist_is_in_list(self, playlist_url, filename):
        """
        :param playlist_url:
        :type playlist_url: str
        :param filename:
        :type filename: str
        :rtype: bool
        """
        return bool(SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_IsInList, pack_s(playlist_url, filename)))

    def playlist_query_playlists(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Playlist_QueryPlaylists, 0)

    def playlist_query_get_next_playlist(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Playlist_QueryGetNextPlaylist, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def playlist_query_files(self, playlist_url):
        """
        :param playlist_url:
        :type playlist_url: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_QueryFiles, pack_s(playlist_url))

    def playlist_query_get_next_file(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Playlist_QueryGetNextFile, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def playlist_query_get_all_files(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Playlist_QueryGetAllFiles, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def playlist_query_files_ex(self, playlist_url):
        """
        :param playlist_url:
        :type playlist_url: str
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Playlist_QueryFilesEx, pack_s(playlist_url))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def playlist_create_playlist(self, folder_name, playlist_name, filenames):
        """
        :param folder_name:
        :type folder_name: str
        :param playlist_name:
        :type playlist_name: str
        :param filenames:
        :type filenames: list of str
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Playlist_CreatePlaylist,
                         pack_sssa(folder_name, playlist_name, filenames))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def playlist_delete_playlist(self, playlist_url):
        """
        :param playlist_url:
        :type playlist_url: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_DeletePlaylist, pack_s(playlist_url))

    def playlist_set_files(self, playlist_url, filenames):
        """
        :param playlist_url:
        :type playlist_url: str
        :param filenames:
        :type filenames: list of str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_SetFiles, pack_ssa(playlist_url, filenames))

    def playlist_append_files(self, playlist_url, filenames):
        """
        :param playlist_url:
        :type playlist_url: str
        :param filenames:
        :type filenames: list of str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_AppendFiles, pack_ssa(playlist_url, filenames))

    def playlist_remove_at(self, playlist_url, index):
        """
        :param playlist_url:
        :type playlist_url: str
        :param index:
        :type index: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_RemoveAt, pack_si(playlist_url, index))

    def playlist_move_files(self, playlist_url, from_indices, to_index):
        """
        :param playlist_url:
        :type playlist_url: str
        :param from_indices:
        :type from_indices: list of int
        :param to_index:
        :type to_index: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_MoveFiles,
                           pack_siai(playlist_url, from_indices, to_index))

    def playlist_play_now(self, playlist_url):
        """
        :param playlist_url:
        :type playlist_url: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_PlayNow, pack_s(playlist_url))

    def playlist_get_item_count(self, playlist_url):
        """
        :param playlist_url:
        :type playlist_url: str
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Playlist_GetItemCount, pack_s(playlist_url))

    def library_get_file_property(self, file_url, file_property):
        """
        :param file_url:
        :type file_url: str
        :param file_property:
        :type file_property: MBFileProperty
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetFileProperty, pack_si(file_url, file_property))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_get_file_tag(self, file_url, field):
        """
        :param file_url:
        :type file_url: str
        :param field:
        :type field: MBMetaData
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetFileTag, pack_si(file_url, field))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_set_file_tag(self, file_url, field, value):
        """
        :param file_url:
        :type file_url: str
        :param field:
        :type field: MBMetaData
        :param value:
        :type value: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Library_SetFileTag, pack_sis(file_url, field, value))

    def library_commit_tags_to_file(self, file_url):
        """
        :param file_url:
        :type file_url: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Library_CommitTagsToFile, pack_s(file_url))

    def library_get_lyrics(self, file_url, lyrics_type):
        """
        :param file_url:
        :type file_url: str
        :param lyrics_type:
        :type lyrics_type: MBLyricsType
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetLyrics, pack_si(file_url, lyrics_type))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_get_artwork(self, file_url, index):
        """
        :param file_url:
        :type file_url: str
        :param index:
        :type index: int
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetArtwork, pack_si(file_url, index))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_get_artwork_url(self, file_url, index):
        """
        :param file_url:
        :type file_url: str
        :param index:
        :type index: int
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetArtworkUrl, pack_si(file_url, index))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_get_artist_picture(self, artist_name, fading_percent, fading_color):
        """
        :param artist_name:
        :type artist_name: str
        :param fading_percent:
        :type fading_percent: int
        :param fading_color:
        :type fading_color: int
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetArtistPicture,
                         pack_si(artist_name, fading_percent, fading_color))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_get_artist_picture_urls(self, artist_name, local_only):
        """
        :param artist_name:
        :type artist_name: str
        :param local_only:
        :type local_only: bool
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetArtistPictureUrls, pack_sb(artist_name, local_only))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_get_artist_picture_thumb(self, artist_name):
        """
        :param artist_name:
        :type artist_name: str
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_GetArtistPictureThumb, pack_s(artist_name))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_add_file_to_library(self, file_url, category):
        """
        :param file_url:
        :type file_url: str
        :param category:
        :type category: MBLibraryCategory
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_AddFileToLibrary, pack_si(file_url, category))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_query_files(self, query):
        """
        :param query:
        :type query: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Library_QueryFiles, pack_s(query))

    def library_query_get_next_file(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Library_QueryGetNextFile, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_query_get_all_files(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Library_QueryGetAllFiles, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_query_files_ex(self, query):
        """
        :param query:
        :type query: str
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_QueryFilesEx, pack_s(query))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_query_similar_artists(self, artist_name, minimum_artist_similarity_rating):
        """
        :param artist_name:
        :type artist_name: str
        :param minimum_artist_similarity_rating:
        :type minimum_artist_similarity_rating: double
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_QuerySimilarArtists,
                         pack_sd(artist_name, minimum_artist_similarity_rating))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_query_lookup_table(self, key_tags, value_tags, query):
        """
        :param key_tags:
        :type key_tags: str
        :param value_tags:
        :type value_tags: str
        :param query:
        :type query: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Library_QueryLookupTable,
                           pack_s(key_tags, value_tags, query))

    def library_query_get_lookup_table_value(self, key):
        """
        :param key:
        :type key: str
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_QueryGetLookupTableValue, pack_s(key))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_jump(self, index):
        """
        :param index:
        :type index: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Library_Jump, index)

    def library_search(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: list of str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_Search, pack_sssa(query, comparison, fields))

        r = unpack_sa(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_search_first(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_SearchFirst, pack_sssa(query, comparison, fields))

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_search_indices(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: list of int
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_COPYDATA, MBC_Library_SearchIndices, pack_sssa(query, comparison, fields))

        r = unpack_ia(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def library_search_first_index(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: int
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Library_SearchFirstIndex,
                           pack_sssa(query, comparison, fields))

    def library_search_and_play_first(self, query, comparison="Contains", fields=["ArtistPeople", "Title", "Album"]):
        """
        :param query:
        :type query: str
        :param comparison:
        :type comparison: str
        :param fields:
        :type fields: list of str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Library_SearchAndPlayFirst,
                           pack_sssa(query, comparison, fields))

    def setting_get_field_name(self, field):
        """
        :param field:
        :type field: MBMetaData
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Setting_GetFieldName, field)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def setting_get_data_type(self, field):
        """
        :param field:
        :type field: MBMetaData
        :rtype: MBDataType
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Setting_GetDataType, field)

    def window_get_handle(self):
        """
        :rtype: HWND
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Window_GetHandle, 0)

    def window_close(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Window_Close, 0)

    def window_restore(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Window_Restore, 0)

    def window_minimize(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Window_Minimize, 0)

    def window_maximize(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Window_Maximize, 0)

    def window_move(self, x, y):
        """
        :param x:
        :type x: int
        :param y:
        :type y: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Window_Move, pack_i(x, y))

    def window_resize(self, w, h):
        """
        :param w:
        :type w: int
        :param h:
        :type h: int
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_Window_Resize, pack_i(w, h))

    def window_bring_to_front(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Window_BringToFront, 0)

    def window_get_position(self):
        """
        :rtype: list of 2 int
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Window_GetPosition, 0)

        r = unpack_ii(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def window_get_size(self):
        """
        :rtype: list of 2 int
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_Window_GetSize, 0)

        r = unpack_ii(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_music_bee_version(self):
        """
        :rtype: MBMusicBeeVersion
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_MusicBeeVersion, 0)

    def get_music_bee_version_str(self):
        """
        :rtype: str
        """
        v = SendMessage(self.find_hwnd(), WM_USER, MBC_MusicBeeVersion, 0)
        if v == MBMBV_v2_0:
            return "2.0"
        elif v == MBMBV_v2_1:
            return "2.1"
        elif v == MBMBV_v2_2:
            return "2.2"
        elif v == MBMBV_v2_3:
            return "2.3"
        else:
            return "Unknown"

    def get_plugin_version_str(self):
        """
        :rtype: str
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_PluginVersion, 0)

        r = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        return r

    def get_plugin_version(self):
        """
        :rtype: list of int
        """
        hwnd = self.find_hwnd()

        lr = SendMessage(hwnd, WM_USER, MBC_PluginVersion, 0)

        v = unpack_s(lr)

        SendMessage(hwnd, WM_USER, MBC_FreeLRESULT, lr)

        v = v.split(".")
        for i in range(len(v)):
            v[i] = int(v[i])

        return v

    def test(self):
        """
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_USER, MBC_Test, 0)

    def message_box(self, text, caption):
        """
        :param text:
        :type text: str
        :param caption:
        :type caption: str
        :rtype: MBError
        """
        return SendMessage(self.find_hwnd(), WM_COPYDATA, MBC_MessageBox, pack_s(text, caption))

    def find_hwnd(self):
        return FindWindow(None, "MusicBee IPC Interface")

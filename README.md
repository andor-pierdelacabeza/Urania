Urania
======

Star photography and tracking system

## What is it (or should be) ?

Urania pretends to be  (in a near future) a complement for your star gazing/photographing activities.

Right now is based in a Raspberry Pi plus the Raspicam module, but the idea is moving to any debian compatible platform and support other external sensors more suited to astrophotography.

I hope it can:

- [x] Do a live view for focusing
- [ ] Time lapse photos
- [ ] Black frames
- [ ] Alignment
- [ ] Stacking
- [ ] Telescope GoTo
- [ ] GPS time sync and photo tagging

## Requirements

### Debian packages

- libcurl4-openssl-dev
- python-dev
- libjpeg-dev

### Python packages

Help yourself into a virtualenv and then: 

`pip install -r reqs.txt`

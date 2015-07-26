# Methods for creating the in-game world

import sys
import random

class World(object):

  worldBiomes = [
    'desert',    # yellow
    'swamp',     # purple
    'forest',    # green
    'snow'       # white
  ]

  specialBiomes = [
    'cave',      # gray
    'indoors',   # brown
    'inferno',   # orange
    'evil'       # red
  ]

  # Generate a world
  def __init__(self, numZones, name=''):
    if name == '':
      name = self._createWorldName()

    self.name = name
    self.zones = []

    for zone in range(numZones):
      self.generateZone()


   # prints the world (for debugging purposes)
  def _printWorld(self):
    print 'Name:\t' + self.name
    print 'Zones:\t' + str(len(self.zones)) + '\n\n'
    print '--- Zones ---'
    for zoneIndex in range(len(self.zones)):
      zone = self.zones[zoneIndex]
      print '\nName:\t' + str(zone['name'])
      print 'Size:\t' + str(zone['size'])
      print 'Biome:\t' + str(zone['biome'])
      print 'Tiles:'
      for x in range(zone['size']):
        for y in range(zone['size']):
          sys.stdout.write(zone['tiles'][x][y]['type'])
        print


  # Adds a zone to the world. Zones are in the format:
  #   {
  #      'name':   string,
  #      'size':   int,
  #      'biome':  string,
  #      'tiles':  [[
  #                {
  #                  'type': string,
  #                  'revealed': bool
  #                }
  #              ]]
  #   }
  #
  # Paramters:
  #   size (integer):  size*10 is the number of tile rows and columns in the zone
  #   biome (string):  Biome type will be used for this zone, see top of class for list.
  def generateZone(self, size='', biome='', name=''):
    if size == '':
      size = random.randint(3, 5)
    if biome == '':
      biome = self.worldBiomes[random.randint(0, len(self.worldBiomes) - 1)]
    if name == '':
      name = self._createZoneName()

    zone = {}

    if not self._verifyBiome(biome):
      biome = self.worldBiomes[0]

    zone['name'] = name
    zone['size'] = size * 10
    zone['biome'] = biome
    zone['tiles'] = self._createPaths(zone['size'])

    self.zones.append(zone)


  def _createZoneName(self):
    return 'UNIMPLEMENTED'

  def _createWorldName(self):
    return 'UNIMPLEMENTED'

  def _createPaths(self, size):
    tiles = []
    for x in range(size):
      row = []
      for y in range(size):
        tile = {}
        tile['type'] = '0'
        tile['revealed'] = False
        row.append(tile)
      tiles.append(row)

    return tiles



  def _verifyBiome(self, biome):
    try:
      self.worldBiomes.index(biome)
    except():
      try:
        self.specialBiomes.index(biome)
      except():
        return False
    return True

# From: https://www.edureka.co/community/19373/how-can-i-read-piano-notes-on-python
import pygame.midi

def print_devices():
    for n in range(pygame.midi.get_count()):
        print (n,pygame.midi.get_device_info(n))

def parseData(data):
    event = data[0][0]
    timestamp = event[1]
    note_number = event[1]
    velocity = event[2]
    note = number_to_note(note_number)
    return note_number, note, velocity

def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number%12]

def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)
            note_number, note, velocity = parseData(event)
            print(note_number, note, velocity)            

if __name__ == '__main__':
    pygame.midi.init()
    print_devices()
    my_input = pygame.midi.Input(0) #only in my case the id is 2
    readInput(my_input)
SHELL = /bin/sh
CC    = gcc

FLAGS   += -I include
CFLAGS  = -fPIC -g
LDFLAGS = -shared

TARGET  = libget_key.so
SOURCES = $(shell echo src/*.c)

all: $(TARGET)

clean:
	rm -f $(OBJECTS) $(TARGET)

install:
    PATH +=

$(TARGET): $(OBJECTS)
	$(CC) $(FLAGS) $(CFLAGS) $(LDFLAGS) -o $(TARGET) $(SOURCES)

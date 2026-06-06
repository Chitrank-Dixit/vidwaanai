# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Mahabharat 0.5531)
- **Original**: किसीके लिये भी असम्भव था, तो भी उसकी चोट सहनेके
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5531)
- **Original**: किसीके लिये भी असम्भव था, तो भी उसकी चोट सहनेके
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5532)
- **Original**: लिये मद्रराज शल्य गरज उठे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5532)
- **Original**: लिये मद्रराज शल्य गरज उठे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5533)
- **Original**: किंतु यह झक्ति उनकी छाती. छेदती हुई शरीरके मर्मस्थानोंकों बिदीर्ण कर पृथ्वीमें समा गयी और राजाका विज्ञाल यज्ञ भी अपने साथ ही छेती
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5533)
- **Original**: किंतु यह झक्ति उनकी छाती. छेदती हुई शरीरके मर्मस्थानोंकों बिदीर्ण कर पृथ्वीमें समा गयी और राजाका विज्ञाल यज्ञ भी अपने साथ ही छेती
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5534)
- **Original**: फिर एक तेज किये हुए भल्लके द्वारा उन्होंने उसका मत्तक
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5534)
- **Original**: फिर एक तेज किये हुए भल्लके द्वारा उन्होंने उसका मत्तक
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5535)
- **Original**: काट लिया। तब खूनसे रैगा हुआ उसका धड़ रथसे नीचे गिर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5535)
- **Original**: काट लिया। तब खूनसे रैगा हुआ उसका धड़ रथसे नीचे गिर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5536)
- **Original**: पड़ा । यह देखकर कौरव-सेनामें भगदड़ पड़ गयी । उस संमय
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5536)
- **Original**: पड़ा । यह देखकर कौरव-सेनामें भगदड़ पड़ गयी । उस संमय
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5537)
- **Original**: सात्यकि भागते हुए कौरवोंपर भी बाण बरसाने लगा, किंतु
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5537)
- **Original**: सात्यकि भागते हुए कौरवोंपर भी बाण बरसाने लगा, किंतु
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5538)
- **Original**: कृतवर्षाने वहाँ पहुँचकर उसे आगे बढ़नेसे रोक लिया। अब
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5538)
- **Original**: कृतवर्षाने वहाँ पहुँचकर उसे आगे बढ़नेसे रोक लिया। अब
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5539)
- **Original**: थे ही दोनों एक-दूसरेपर बराणोंकी बौछार करने छगे। गयी। उनका सारा अड्डु छिन्न-धिनत्र हो गया और वे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5539)
- **Original**: थे ही दोनों एक-दूसरेपर बराणोंकी बौछार करने छगे। गयी। उनका सारा अड्डु छिन्न-धिनत्र हो गया और वे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5540)
- **Original**: कृतवर्माने दस बाणोंसे सात्यकिको और तीनसे उसके ल्लेहूलुह्मम होकर प्रेमसे पृथ्यीका आलिड्डन. करते हुए-से
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5540)
- **Original**: कृतवर्माने दस बाणोंसे सात्यकिको और तीनसे उसके ल्लेहूलुह्मम होकर प्रेमसे पृथ्यीका आलिड्डन. करते हुए-से
- **Translation**: 

---


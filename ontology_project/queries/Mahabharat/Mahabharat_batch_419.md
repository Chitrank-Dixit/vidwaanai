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

### Verse 1 (Mahabharat 0.4181)
- **Original**: 5 देने लगा। महान्‌ धनुर्धर कर्णको व्यूहके मुहानेपर कवच
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4181)
- **Original**: 5 देने लगा। महान्‌ धनुर्धर कर्णको व्यूहके मुहानेपर कवच
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4182)
- **Original**: धारण किये उपस्थित देख कौरब योद्धा द्रोणाचार्यके
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4182)
- **Original**: धारण किये उपस्थित देख कौरब योद्धा द्रोणाचार्यके
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4183)
- **Original**: वियोगका दुःख भूल गये।
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4183)
- **Original**: वियोगका दुःख भूल गये।
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4184)
- **Original**: तदनन्तर कर्ण तथा अर्जुन आमने-सामने आकर खड़े
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4184)
- **Original**: तदनन्तर कर्ण तथा अर्जुन आमने-सामने आकर खड़े
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4185)
- **Original**: हुए और दोनों एक-दूसरेको देखते ही क्रोधमें भर गये
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4185)
- **Original**: हुए और दोनों एक-दूसरेको देखते ही क्रोधमें भर गये
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4186)
- **Original**: कर्णपर्व विन्द-अनुविन्द और चित्रसेत तथा चित्रक्वा वध, अश्वत्यामा और घीमसेनका भयंकर युद्ध ईे सेकनेसे भी नहीं रूका। क्षेमधूर्तिने किसी तरह हाथीको
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4186)
- **Original**: कर्णपर्व विन्द-अनुविन्द और चित्रसेत तथा चित्रक्वा वध, अश्वत्यामा और घीमसेनका भयंकर युद्ध ईे सेकनेसे भी नहीं रूका। क्षेमधूर्तिने किसी तरह हाथीको
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4187)
- **Original**: कूदकर नीचे आ गया और तलबार उठाकर भीमसेनकी काबूमें किया और क्रोधमें भरकर भीमसेनको बाणोंसे बींथ
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4187)
- **Original**: कूदकर नीचे आ गया और तलबार उठाकर भीमसेनकी काबूमें किया और क्रोधमें भरकर भीमसेनको बाणोंसे बींथ
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4188)
- **Original**: ओर दौड़ा। यह देख भीमने उसपर गदासे चोट की। डार्ता। साथ. ही उनके हाथीके... भी... मर्मस्थानोंमें छोट
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4188)
- **Original**: ओर दौड़ा। यह देख भीमने उसपर गदासे चोट की। डार्ता। साथ. ही उनके हाथीके... भी... मर्मस्थानोंमें छोट
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4189)
- **Original**: उसके आधातसे क्षेमधूर्तिके प्राण-पसखेरू उड़ गये और पहुँचायी। हाथी उस आधातको न सह सका। वह गआ्राण
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4189)
- **Original**: उसके आधातसे क्षेमधूर्तिके प्राण-पसखेरू उड़ गये और पहुँचायी। हाथी उस आधातको न सह सका। वह गआ्राण
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4190)
- **Original**: वह तलवारके साथ ही हाथीके पास गिर पड़ा। महाराज ! स्थागकर पृथ्वीपर गिर पड़ा। भीमसेन उसके गिरनेसे पहले
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4190)
- **Original**: वह तलवारके साथ ही हाथीके पास गिर पड़ा। महाराज ! स्थागकर पृथ्वीपर गिर पड़ा। भीमसेन उसके गिरनेसे पहले
- **Translation**: 

---


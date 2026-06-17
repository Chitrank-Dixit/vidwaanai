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

### Verse 1 (Bhagwat_Geeta 115.999)
- **Original**: दिवि सूर्यसहस्त्रस्य भवेद्युगपदुत्थिता। यदि भा: सदूशी सा स्याद्धासस्तस्य महात्मन:
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 115.1000)
- **Original**: आकाशमें हजार सूर्योके एक साथ उदय होनेसे
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 115.1001)
- **Original**: श्डड * श्रीमद्धगवद्रीता * उत्पन्न जो प्रकाश हो, वह भी उस विश्वरूप परमात्माके प्रकाशके सदृश कदाचित्‌ ही हो
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 115.1002)
- **Original**: तत्रैकस्थं जगत्कृत्स्नं प्रविभक्तमनेकधा। अपश्यदेवदेवस्थ शरीरे पाण्डवस्तदा
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 115.1003)
- **Original**: पाण्डुपुत्र अर्जुन उस समय अनेक प्रकारसे विभक्त अर्थात्‌पृथक्‌-पृथक्‌ सम्पूर्ण जगतको देवोंके देव श्रीकृष्ण- भगवान्‌के उस शरीरमें एक जगह स्थित देखा
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 115.1004)
- **Original**: ततः स विस्मयाविष्टो हष्टरोमा धनज्जयः। प्रणम्य शिरसा देव कृताझ्ललिरभाषत
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 115.1005)
- **Original**: उसके अनन्तर वे आश्चर्यस। चकित और पुलकितशरीर अर्जुन प्रकाशमय विश्वरूप परमात्माको श्रद्धा-भक्तिसहित सिरसे प्रणाम करके हाथ जोड़कर बोले--
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 115.1006)
- **Original**: अर्जुन उवाच पश्यामि देवांस्तव देव देहे सर्वास्तथा भूतविशेषसड्डान्‌। बरह्याणमीशं कमलासनस्थ- मृषीश्व सर्वानुरगांश्व दिव्यान्‌
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 115.1007)
- **Original**: अर्जुन बोले-हे देव! में आपके शरीरमें सम्पूर्ण देवोंको तथा अनेक भूतोंके समुदायोंको, कमलके आसनपर विराजित ब्रह्माको, महादेवको और सम्पूर्ण
- **Translation**: 

---


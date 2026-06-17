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

### Verse 1 (Vishnu Puran 0.13361)
- **Original**: तस्पात्ता ररभेए् 23.
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13362)
- **Original**: तत्मादपि महारपप- 109.
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13363)
- **Original**: स्स्मात्रन हमिष्कसि धंड.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13364)
- **Original**: तरमादपि झात्ति: 71
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13365)
- **Original**: तस्प्रशाद्ररसुझञकः श्थ्‌ 67.
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13366)
- **Original**: तम्मात्सावभौमः 25
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13367)
- **Original**: ठममारपेंग खाटेन 32
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13368)
- **Original**: व्स्मोेयक्षसतसवापि 30.
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13369)
- **Original**: उस्मादष्शधिसीमकश्ण: #4..
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13370)
- **Original**: ठस्मादपष्पिमा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13371)
- **Original**: सुता: आज्ञा: अध्यन इत्पेन 5:13 है. डे उजश3 46 है है? रे डे डर ] 5... शृष्ठतत 3 हढड 'डजरंड 596 च्कन्लड है 5 ःछफातड्ाडइर्‌ 2 रैइ श7 डे 18 रद डे 618 है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13372)
- **Original**: ] #. छ 6 4.- 298 3 हु: करे 8 डे 11 10 डे 30 259 5 #ीएआ 5105 3393 202... हा है है. बृ 4 हे. रैंदछ0 7927 3 68 5 के एैं6 श्र हे 5 रए के शुए (हर केक 43 54 शी । इज: हुए 609 3 115- एइण्3 दे रैर3 7छत ब्र 8 11 करंट र8 8 हे8 63 5 बे8 689 छू 5 29 + 3043 72... ् शृदु प््छ 19 59 4 219 ड़ ड़ 10 है । दे ऋश्ट/ए!/ 6 डे भर अरे डेटलर1 ह्‌ डे कररशुता हर
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13373)
- **Original**: इस्लेकाः अंश्ञाः अध्य' इत्पे- इस्प्रेफ: अंक: अध्यार इले* ठा्माशोदयन उदयनास्‌ 4 रह: 15-
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13374)
- **Original**: तस्मात्रजाहिताथीय ». श33ह उला80 गप्माएुल्क्यरतस्माण 4 394 +6-
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13375)
- **Original**: तस्वशदद स्तोक्रेण 1/47930:9757 तम्नात्सहदेय: ».. डे 22 4 4
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13376)
- **Original**: गस्मातुपुस्फरेवो 31 337 ह< 38 तस्मादर्भ$- डे 24 8 (80
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13377)
- **Original**: खाते दुःखबहल: 1 0#पुए3छ118 तत्मादोद्यर:: 4-0 4 7716.
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13378)
- **Original**: रफमप्रेव महायज्े $ ईहे रे तस्माच्छुणुष्न रजेन्र 3 838 75: .
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13379)
- **Original**: रस्मनिजते तु भूतानि 1 ।37
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13380)
- **Original**: 441 टस्मदापे नन्दिक्सन 4 24: 17
- **Translation**: 

---


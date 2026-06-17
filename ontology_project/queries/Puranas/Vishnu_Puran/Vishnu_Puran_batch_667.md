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

### Verse 1 (Vishnu Puran 0.13321)
- **Original**: तेड्शाथक्ाप्त 13 49 तदेभागल्मत्यर्थम्‌ 3- (9 - 36
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13322)
- **Original**: तदवष्टिजनिते सस्यम्‌ 75 8 10 8-8 20 सदेडरूध्यत सर्च 6 66 « 36
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13323)
- **Original**: तरया धदकिलायाः 5 32 के रैक मयात्यागम्‌ 6 67: 77.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13324)
- **Original**: तख्मसलतिसंज्ञश 4. 188 श्डट रादेशमतिदु:/खात्रम्‌ 6 67888077 .
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13325)
- **Original**: तनारशुरिफ्तला: 50 5 हर तेज गोष्मध्ये यु 6-69 + 66
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13326)
- **Original**: तंब्रिमोध यथा सर्े 3.03 732 तदेव सर्मेवतत्‌ 6 2-0 5 श्ड
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13327)
- **Original**: तज्ूनमत्य सकादो डे :13/ 47134 तदेतदक्षर नित्यम्‌ 6 23-87 6ै+*
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13328)
- **Original**: तआपत पोते पुत्रा: है शेडत 11 तदेवाप्लर्द फर्म 2 श््ध 25 ।तसस्ल॑प्रगनायत्यम्‌ 3 (4 5 श1 तदेशद्ूपता काला 2 34 5 36
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13329)
- **Original**: तम्मंत्ता चविश्ामिपम्‌ 4 ह्/079%ऐरे तंदेय प्रीठये भूल' 27744:67008048/
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13330)
- **Original**: ठत्मात्राणौद्वितीयश्ष है ता ब्छु सका ए0
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13331)
- **Original**: श् हर हैँ 2. 4 कई त उस 40 कई 26 >7 5 69 6 शक ल्‍एप ल्‍क न मी #फ अत बुध 40 ऋए आ बा म# कई हाई 2 7 2 6 2 #0 4 40 7 #4 ल्‍न ह0 0 & ++ ++
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13332)
- **Original**: नल जानी >0 >> 77 964: 7 0 7 4 > डे 676:457.000+# 7» ऊ श्र 62] 48 श्5्‌ 45 श्र ः्श्‌0 नो ढक (489) ड्लः डेप.
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13333)
- **Original**: तम्नेशाय इटोकः 16.
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13334)
- **Original**: तयोहश्ञागपादस्य £
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13335)
- **Original**: तयोक्ष रमतिभीषरम्‌ <5
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13336)
- **Original**: तरत्यकिशां विक्ताम्‌ 20.
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13337)
- **Original**: तस्वल्कलापर्गटीर- 31.
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13338)
- **Original**: ठह्लिए्सुरसुरमठत्र 35.
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13339)
- **Original**: त्वाझगुस्मैश्वर्शम्‌ 1
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13340)
- **Original**: ह्वोफेश्तदानाथ 4.
- **Translation**: 

---


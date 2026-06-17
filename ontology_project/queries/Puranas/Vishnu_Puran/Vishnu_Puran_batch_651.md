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

### Verse 1 (Vishnu Puran 0.13001)
- **Original**: अतिदुश्संद्ारिण: 2 115 9151
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13002)
- **Original**: अतितिक्षायन क़्रम्‌ 4 18 15
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13003)
- **Original**: अतिविर्यस्थ भग्राशः 2 7 <
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13004)
- **Original**: अतिथिर्य॑स्थ भग्मादाः द्रे हु 28 अतिथि णगते तव 4ड 6 13
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13005)
- **Original**: अतिथि तत्र सप्प्रपरम्‌ 1 15 81
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13006)
- **Original**: अतिवेगितया कलम्‌ 7 4ड
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13007)
- **Original**: अतिभीमा समागम्य मत नए खत जर 4त बात 29 कक“ #*4ं कई #%9. # 8
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13008)
- **Original**: # धर उके मई न न खा क्री को /1 नए > आ न कई # #ई # .,छ 6 # 7 #ऋ अड 80 श्र 7 हरे. रे 38 25 44 19 13 र्छ 13 5 28 19 19 29 19 हे0 है9 हे3 19 56 19 4 6-4 5 1 35 ह.। €्द्ध बे 34 हैंड । 5. रे5 5 र1 शहर इर
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13009)
- **Original**: रछ श्र 15 श्र ड5 1 पड ्‌ डरे 4 9 6 । है 18. 30 श्र 1 1 29 12 26 रू हृणढड 17 23 श्र 68 रु 15 हू 10 11 59 <.. हेई ह8 क्ड
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13010)
- **Original**: सत्मेका:ः ओडज्ञा: अध्या" बस्ले* इरत्प्रेका: अदा: अध्या&. इस्ोः अंबीता वर्तमाना
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13011)
- **Original**: 74. #&0+ शेड: 8103...
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13012)
- **Original**: अथ क्षार्महातनयम्‌ “*. &48/11778 7417 अरब ब्रोडिल याला 7». 38 31688: 68.
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13013)
- **Original**: अथलैनों सन्दनम्‌ हा. 4 7334 21 अरीतकल्पानताने रैलाउगर्ड 3. अध तादवबरूप्छोपसेन" 4: 13 116 अतैतानागतानौह 3 0: 56: 5
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13014)
- **Original**: अथदुर्वसोव॑शपवधास्य 46167 419 अतँव जाएरखप्रे 3 62 5 17
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13015)
- **Original**: अथवा कि क्यत्मौ: 5424 15 अते गकस्स भगवान्‌ 5 38 62
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13016)
- **Original**: अथवा याद; सेहः 50 277 रेड अठे मदर नाभ्णाम्‌ 2-78 -है9
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13017)
- **Original**: अथवा कौवाबासप्‌ 6 53578 33 अगेडड्मस्व पोज छ्ो* 4 “138 187
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13018)
- **Original**: अधतसमुत्ंचसौे 5 348 18 अतेषओए ममाओषमस 4 7- रेरे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13019)
- **Original**: अधहर्फप्नोफनोच 3 छात्डः 7-17 अल: प्रोषकल्पीकचेल: 4-40 रे. अधर्यदेर्द स मुनि: 3746 है अतः परे ययातेः 4 74313 32.
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13020)
- **Original**: अथ भुड्ठे गृहे तस्य *«« 1ै4++18108- 46 अतः संम्ग्रणते लग: श्फेपरते 4.
- **Translation**: 

---


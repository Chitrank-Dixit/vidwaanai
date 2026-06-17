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

### Verse 1 (Vishnu Puran 0.13021)
- **Original**: अवखापिन 4...
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13022)
- **Original**: 44 2530 अछ पर मकिपयानत्म डे र1 3
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13023)
- **Original**: अय पृष्टा पुत्रप्प्यक्वीत्‌ 45:716888043 अचे गधा बाधववबडिकम्भु 58768 ब0.
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13024)
- **Original**: अधतनदगत्य डे 7 डे अलक्ताधुशकूप* *% 7 - 31 6 अयभगवान्‌पितामहः 4:076: के1 असत्य्तकरवीशोा" & 4 16
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13025)
- **Original**: अवाजगाप तलीरप्‌ «7» रे 13 213 अत्यर्च्यित सोडप्रथ 38 127 58
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13026)
- **Original**: अधान्यमप्युरणकमादाय » डाटआइए > 55 अत्यनत्तमिताक्नाम्‌ 1:17 “616
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13027)
- **Original**: अवाह याउवल्कदसु 3 75 8 अत्यार्सजगतरस््राणास 4 4 15
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13028)
- **Original**: अवबाद भगजात्‌ 5 अमप्न हि ग़ज्ञे युथवाश्वश्य 4 2-75
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13029)
- **Original**: अथाह कृष्णमकूएः 57 18 -ढढ अग्र इत्मेक; 23044 3. अयागत््य देवगजोउअवीत्‌ डएए 3. 680 अन्न जन्पसहस्राणामू 2 जे 23
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13030)
- **Original**: अय्न्तर्जलायस्थितः 54 फ्े
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13031)
- **Original**: 29:1 अन्न हिं सं्रो डे 23 “2
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13032)
- **Original**: अधाक्रपक्षीयैभेजि: 4 3 शहर अन्न व रस्लेकः डे दे 62
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13033)
- **Original**: अधाहक्कूर स एपः 4. 4 7788 शड8 अन्न देनासपा दैत्या। 6 48 « शड
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13034)
- **Original**: अयान्तरिक्षे कागु्ेः ऐु50791:0474:7 अन्रानुवैद्ञस्छोकों भवति 34 100 5
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13035)
- **Original**: अधान्तरिक्षे वागु्ः *. 47 - 288 21 अन्ना इल्ेकः ड 215 17
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13036)
- **Original**: अधाहानितो विप्र छा ह313108त18 अज्नामुरवशश्छोकः डे - 22 ।1स
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13037)
- **Original**: अधोपजापि खर्दताअम्‌ इस्टकनरड00 7427 अजावतोर्षयो: कृष्ण 5 77 :ड1
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13038)
- **Original**: अथैतागफत्ीठामागत* 4 7430 031 अगन्तों य सगरः 4: डे. 36 । अर्थनावसि्रे जीक्पूतकरत्‌ हंटफ 397 4के अति भारत॑ ठेप्रम्‌ 207 27 #ठरेर 4/770677781 अफ्रपि श्रुष्पो झप्रेझ: 4 4 541
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13039)
- **Original**: अ्ैनंटेयर्षय:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13040)
- **Original**: /333 2 अस्विसिश्ले यदि 95 7 “727
- **Translation**: 

---


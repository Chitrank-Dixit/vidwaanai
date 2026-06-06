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

### Verse 1 (Vishnu Puran 0.641)
- **Original**: जबह्मयाजीने पहले जिन सनन्‍दनादिकों उत्पन्न किया था जे निरपेक्ष होनेके कत्ररण सत्तान और संसार आदियें प्रबतत नहीं हुए
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.642)
- **Original**: वे सभी ज्ञानसम्पन्न , विरक्त और मत्सरादि दोषोंसे रहित थे। उन महात्माओको संसार-रचनासे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.643)
- **Original**: श्ड ब्रह्मणो5भून्महान्‌ क्रोधस्ैत्मेक्यद्हनक्षम: । तप क्रोधात्समुद्धृतज्वालापालातिदीपितम्‌ । ब्रह्मणो5भूत्तदा सर्व त्ैल्लोक्यमस्विलं मुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.644)
- **Original**: 19 भ्रकुटीकुटिलात्तस्थ ललायत्क्रोधदीपितात्‌ । समुत्पन्नस्तदा रुद्रो मध्याह्रार्कसमप्रमः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.645)
- **Original**: 12 अर्धनारीनरबपु: प्रचण्डो5तिहरीरवान्‌ । विभजात्मानमित्युकत्या त॑ ब्रह्मात्तर्दघे ततः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.646)
- **Original**: 13 तथोक्तोउसौ द्विधा ख्रीलं पुरुषत्व॑ तथाउकरोत्‌ । बिभेदपुरुषत्व॑ चर दशाधा चैकथा पुनः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.647)
- **Original**: 14 सौम्यासोम्यैस्तदा झात्ताउशात्तै: खीलं चस प्रभु: । विभेद बहुधाः देव: स्वरूपैरसितेः सितैः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.648)
- **Original**: 15 ततो ब्रह्मा55त्मसम्भूत॑ पूर्व स्वायम्पुर्व प्रभु: । आत्मानमेव कृतवान्य्रजापाल्ये मनुं द्विज
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.649)
- **Original**: 16 झतरूपां च तां नारों तपोनिर्धूतकल्मषाम्‌ । स्वायम्भुवो मनुर्देव: पत्नीत्वे जगूहे प्रभुः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.650)
- **Original**: 17 तस्मान्तु पुरुषादेवी शतरूपा व्यजायत। प्रियव्रतोत्तानपादी प्रसूत्याकृतिसंज्ञितम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.651)
- **Original**: 18 कन्याद्रयं च॒ धर्मज्ञ रूपोदार्यगुणान्वितम्‌ । ददौ प्रसूति दक्षाथ आकूति रुचनये पुरा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.652)
- **Original**: 19 प्रजापति: स॒ जग्राह तयोर्जज्ञे सदक्षिण: । पुत्रो यज्ञो महाभाग दम्पत्योर्मिथुनं तत:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.653)
- **Original**: 20 यज्ञस्य दक्षिणायां तु पुत्रा द्वादश जज्षिरे। यामा डति समाख्याता देवा: स्वायम्भुे मनौ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.654)
- **Original**: 21 चसूत्यों च तथा दक्षक्षतस्नो विंशतिस्तथा । ससर्ज कन्यास्तासां च सम्यडः नामानि में शूणु
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.655)
- **Original**: 22 श्रद्धा लक्ष्मीर्धृतिस्तुष्टिमेंघा पुष्टिस्तथा क़िया। बुद्धिर्लजा वपु: शान्ति: सिद्धि: कोर्तिख्रयोदशी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.656)
- **Original**: 23 पल्यर्थ प्रतिजग्राह धर्मो दाक्षायणी: प्रभु: । ताध्यः शिष्टा: यवीयस्य एकादश सुल्मेजना:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.657)
- **Original**: 24 ख्याति: सत्यथ साभूति: स्मृति: प्रीति: क्षमा तथा । सन्ततिआ्रानसूया च ऊर्जा स्वाहा स्वधा तथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.658)
- **Original**: 25 भृगुर्गवों मरीचिश्न तथा चैवाड्लिरा मुनि: । पुलस्त्य: पुलहश्चैब॒क्रतुश्षर्षिबरस्तथा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.659)
- **Original**: 26 आविए्णुपुराण [ अ0 7 ब्रद्माजीको प्रिक्लोकोकों भस्म कर देनेवाला मह्मन्‌ क्रोध उत्पन्न हुआ। है मुने ! उन ब्रह्माजोके क्रोघके करण सम्पूर्ण त्रिलोकी ज्वाला-मालाऑसे अत्यन्त देदीप्यमान हो गयी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.660)
- **Original**: उस सघय उनकी टेढी भुकुटि और क्रोध-सन्तप्त लखाटसे दोपहरफे सूर्यक समान प्रक्‍्य्रदामान रुद्गको उत्पत्ति हुई
- **Translation**: 

---


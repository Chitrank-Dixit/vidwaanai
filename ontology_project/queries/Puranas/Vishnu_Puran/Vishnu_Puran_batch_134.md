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

### Verse 1 (Vishnu Puran 0.2661)
- **Original**: जिनके विष्यमें तुमने पूछा था वे परम भगवद्धक्त मह्ममति दैत्यप्रबर प्रह्मादजी ऐसे प्रभावशाली हुए
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2662)
- **Original**: उन महात्मा प्रह्मदजीके इस चरिक्रको ओ पुरुष सुनता है उसके पाप ज्ञीघ्र ही नष्ट हो जाते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2663)
- **Original**: हे मैत्रेय ! इसमें सन्देह नहीं कि मनुष्य प्रहाट-चरित्रके सुनने या पढ़नेसे दिन-णतके (निरन्तर) किये हुए पापसे अवश्य छूट जाता है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2664)
- **Original**: हे द्विज ! पूर्णिमा, अमावास्या, अष्टमी अथवा द्वादशीको इसे पढ़नेसे मनुष्यको गोदानका फल मिलता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2665)
- **Original**: जिस प्रकार भगवानते प्रह्लादजीकी सम्पूर्ण आपत्तियोंसे रक्षा की थी उसी प्रकार वे सर्वदा उसको भी रक्षा करते हैं जो उनका चरित्र सुनता है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2666)
- **Original**: कफ्ज्ता नै ऊक्क्या इति श्रीविष्णुपुराणे प्रथमेंडरो विंशोउध्यायः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2667)
- **Original**: श्रीविष्णुपुराण [ अः 21 इक्कीसवाँ अध्याय कदइयपजीकी अन्य स्त्रियोंके वंद्रा एवं मरुद्षणकी उत्पत्तिका वर्णन औपराशर उवाच स॑ह्वादपुत्र आयुष्पाव्छिबिबष्किल एव च। विरोचनस्तु प्राह्मादिबलिरजज्ञे विरोचनात्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2668)
- **Original**: 9 बले: पुत्रशतं त्वासीद्वाणज्येप्ठट महामुने । हिण््याक्षसुताश्षासन्सर्व एवं महाब॒ला:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2669)
- **Original**: 2 उत्कुरः शकुनिश्चैव भूतसन्तापनस्तथा । महानाभो महाबाहु:ः कालनाभस्तथापर:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2670)
- **Original**: 3 अभवन्‍दनुपुत्राश्न॒द्ठिमूर्दा शम्बरस्तथा। 'एकचक्रो महायाहुस्तारकश्च॒ महाबल: । स्वर्भानुर्वृषपर्वा च पुलोमश्च महाबल:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2671)
- **Original**: 5 एते दनोः सुताः ख्याता विप्रचित्तिश्न वीर्ववानू
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2672)
- **Original**: 6 स्वर्भानोस्तु प्रभा कन्या शर्मिष्ठा वार्षपर्वणी । उपदानी हयशिराः प्रख््याता वरकन्यका:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2673)
- **Original**: 7 वैश्वानरसुते चोभे पुल्लेमा कालका तथा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2674)
- **Original**: उधे सुते महाभागे मारीचेस्तु परिग्रह:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2675)
- **Original**: 8 ताभ्यां पुत्रसहल्नाणि पष्टिदानिवसत्तमा: । पौलोगा: कालकेयाश्व मारीचतनया: स्पृता:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2676)
- **Original**: 9 ततो5परे महावीर्या दारुणास्त्वतिनिर्धुणा: । सिंहिकायामथोत्पन्ना विप्रचित्ते: सुतास्तथा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2677)
- **Original**: 10 व्यंः इल्यश्न बलवान्‌ नभश्चैव महाबल: । बातापी नमुचिश्षैव इल्चछ: खसुमस्तथा
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2678)
- **Original**: 11 अन्धको नरकश्जैब कालनाभस्तथैव च। स्वर्भानुश्ष महात्रीयों वरक्त्रयोधी महासुरः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2679)
- **Original**: 12 एतेषां पुत्रपौत्राश्ष झतशोईथ सहद्नश:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2680)
- **Original**: 13 प्रह्लादस्य तु दैत्यस्थ निवातकब्चाः कुले । समुत्पन्ना: सुमहता तपसा 'भावितात्मन:
- **Translation**: 

---


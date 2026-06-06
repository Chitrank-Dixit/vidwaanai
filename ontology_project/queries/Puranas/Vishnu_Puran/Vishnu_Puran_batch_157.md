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

### Verse 1 (Vishnu Puran 0.3121)
- **Original**: हे मुनिसत्तम ! उनमें सुरम्य नगर तथा उपवन हैं और रूक्ष्मी, विष्णु, अग्नि एवं सूर्य आदि देवताओँके अत्यन्त सुन्दर मन्दिर हैं जो सदा किन्नसश्रेश्लोंस सेवित रहते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3122)
- **Original**: उन सुन्दर पर्जत-ड्रोणियोंमें गन्धर्व, यक्ष, राक्षस, दैत्य और दानवादि अहर्निद्ा क्रोड़ा करते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3123)
- **Original**: ऐ मुने
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3124)
- **Original**: ये सम्पूर्ण स्थान भौम (पृथिवीके) स्वर्ग कहलाते हैं; ये धार्मिक पुरुषोंके निवासस्थान हैं। पापकर्मा पुरुष इनमें सौ जन्ममें भी नहीं जा सकते
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3125)
- **Original**: हे द्विज ! आ्रीविष्णुभगवान्‌ भद्गाश्चवर्षमें हयमीज- रूपसे, केतुमालवर्षमें कग़हरूपसे और भारतयर्पमें कूर्मरूपसे रहते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3126)
- **Original**: तथा वे भक्तप्रतिपाल्क श्रीगोविन्‍्द कुरुवर्षमें मत्स्यरूपसे रहते हैं। इस प्रकार के सर्वमय सर्वगामी हरि विश्वरूपसे सर्वत्र ही रहते हैं। हे मैत्रेय / ले सबके आधारभूत और सर्वात्मिक हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3127)
- **Original**: हे महामुने
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3128)
- **Original**: किम्पुरुष आदि जो आठ वर्ष हैं उनमें शोक, श्रम, उद्बेग और श्षुघाका भय आदि कुछ भी नहीं है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3129)
- **Original**: बहाँकी प्रजा स्वस्थ, आतक्ुहीन समस्त दुःखोंसे रहित है तथा वहाँके स्मेग दस-खारह हजार वर्षकी स्थिर आयुवाले होते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3130)
- **Original**: उनमें वर्षा कभी नहीं होती, केवल पार्थिब जल ही है और न उन स्थानोंमें कृतत्रेतादि युगोंको हो कल्पना है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3131)
- **Original**: हे द्विजोत्तम ! इन सभी वर्षो्मे सात-सात कुलपर्वत हैं और उनसे निकली हुई सैकड़ों नदियाँ हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3132)
- **Original**: +-++ # --- इति श्रीविष्णुपुराणे द्वितीयेंकशे द्वितीयोउध्यायः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3133)
- **Original**: अमान रे ज+न+-न
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3134)
- **Original**: 112 श्रीविष्णुपुराण [ आ* 3 तीसरा अध्याय भारतादि नौ खण्डोंका विभाग अऔीपराशर उवाच उत्तर यत्समुद्रस्य हिमाद्रेश्रैव दक्षिणम्‌। वर्ष तद्धारतं नाम भारती यत्र सनन्‍्तति:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3135)
- **Original**: 9 नवयोजनसाहस््नो विस्तारोउस्यथ महामुने । कर्मभूमिरियं स्वर्गमपवर्ग क्र गच्छताम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3136)
- **Original**: रे महेनद्रो मलय: सह्याः शुक्तिमानृक्षपर्वत: । विश्यक्ष पारियात्रश्न सप्तात्र कुछपर्वता:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3137)
- **Original**: 3 अतः सम्प्राप्यते स्वर्गों मुक्तिमस्मात्मयान्ति वै । तिर्यक्त्व॑ नरक॑ च्ञापि यान्त्यत: पुरुषा मुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3138)
- **Original**: 4 इत:ः स्वर्गश्न मोक्षश्न मध्य चान्तश्न गप्यते । न खल्वन्यत्र मर्त्यनां कर्म भूमौ विधीयते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3139)
- **Original**: 5 भारतस्थास्थ॒वर्षस्थ नवभेदाप्निश्ञामय । इन्द्रह्मीप: कसेरुक्ष ताम्रप्णों ग्भास्तिमान्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3140)
- **Original**: 6 नागद्वीपस्तथा सौम्यो गय्धर्वस्त्वथ वारुण: । अर्य॑ तु नवमस्तेषां द्वीप: सागरसंबृत:
- **Translation**: 

---


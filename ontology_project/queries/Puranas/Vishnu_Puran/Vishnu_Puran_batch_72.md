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

### Verse 1 (Vishnu Puran 0.1421)
- **Original**: 82 ल्वमासीर्त्राह्मण: पूर्व मय्येकाप्रमति: सदा । मातापित्रोश्न॒ शुश्रूषुर्निजधर्मानुपाछक:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1422)
- **Original**: 83 कालेन गछ्छता मित्न॑ राजपुत्रस्तवाभवत्‌ । यौवनेडखिलभोगाक्यों. दर्शनीयोग्ज्वलाकृति:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1423)
- **Original**: 84 तत्सड्जात्तस्य तामृद्धिमवल्लोक्यातिदुर्लभाम्‌ । भवेय॑ राजपुत्रो >स्‍हमिति बाउछा त्वया कृता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1424)
- **Original**: 85 अ्रीविष्णुपुराण [ अ« 12 करनेवाले होनेसे सब कुछ आप ही हैं; सब कुछ आपहीसे हुआ है; अतप्‌व सबके ड्वाय आप ही हो रहे हैं इसलिये आप सर्वात्माको नमस्कार है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1425)
- **Original**: है सर्वेश्वर ! आप सर्वात्मक हैं; क्योंकि सम्पूर्ण भूतोंमें व्याप्त हैं; अत: मैं आपसे क्‍या कहूँ ? आप स्वयँ ही सय हृदयस्थित बातोंको जानते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1426)
- **Original**: हे सर्वात्मन्‌ ! हे सर्वभूतेश्वर ! हे सब भूतोंके आदि-स्थान ! आप सर्वभूतरूपसे सभी प्राणियोंकि मनोरथोंकोी जानते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1427)
- **Original**: हे नाथ ! मेरा जो कुछ मनोरथ था वह तो आपने सफल कर दिया और हे जगत्पते ! मेरी तपस्या भी सफल हो गयी, क्योंकि मुझे आपका साक्षात्‌ दर्दन प्राप्त हुआ
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1428)
- **Original**: श्रीभगवान्‌ खोत्ठे---हे घुब ! तुमको मेरा साक्षात्‌ दर्यन प्राप्त हुआ, इससे अवश्य ही तेरी तपस्या तो सफल हो गयी; परन्तु हे राजकुमार ! मेरा दर्शन भी तो कभी निष्फल नहीं होता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1429)
- **Original**: इसलिये तुझकों जिस वरकी इच्छा हो वह माँग ले । मेरा दर्शन हो जानेपर पुरुषको सभी कुछ प्राप्त हो सकता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1430)
- **Original**: ध्रुव बोले--हे धूतभय्येधर भगवन्‌! आप सभीके अन्तःकरणॉमें विराजमान हैं। हे कहमन्‌! मेरे मनक्री जो कुछ अभिल्मषा है वह क्या आपसे छिपी हुई है?
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1431)
- **Original**: ते भी, हे देवेश्वर ! मैं दुर्विनीत जिस अति दुर्लभ वस्तुकी हृदयसे इच्छा करता हूँ उसे आपकी आज्ञानुसार आपके प्रति निवेदन करूँगा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1432)
- **Original**: है समस्त संसारकों रचनेवाले परमेश्वर ! आपके प्रसन्न होनेपर (संसारमें) क्‍या दुर्कम है? इन्द्र भी आपके कृपाकयक्षके फलरूपसे ही त्रिल््ेकीक् भोगता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1433)
- **Original**: प्रभो ! मेरी सौतेली माताने गर्वसे अति बढ़-बढ़कर मुझसे यह कहा था कि 'जो मेरे उदरसे उत्पन्न नहीं है उसके योग्य यह राजासन नहीं है'
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1434)
- **Original**: अतः हे प्रभो । आपके प्रसादसे मैं उस सर्वोत्तम एवं अव्यय स्थानको प्राप्त करना चाहता हैँ जो सम्पूर्ण विश्वका आधारभूत हो
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1435)
- **Original**: श्रीभगवान्‌ बोले--अरे बालक ! तुने अपने पूर्वजन्पपें भी मुझे सन्तुष्ट किया था, इसलिये तू जिस स्थानकी इच्छा करता है उसे अवश्य प्राप्त करेगा
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1436)
- **Original**: पूर्व-जन्ममें तू एक ब्राह्मण था और मुझमें स्वधर्मका पालन करनेवाला था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1437)
- **Original**: कालान्तसमें एक राजपूत्र तेख सित्र हो गया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1438)
- **Original**: वह अपनी युवावस्थामें सम्पूर्ण भोगोंसे सम्पन्न और अति दर्शनीय रूपलावण्ययुक्त था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1439)
- **Original**: उसके सम्से उसके दुर्कभ वैभवकों
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1440)
- **Original**: आ0 12 ] ततो यथाभिलकफिता प्राप्ता ते राजपुत्रता । उत्तानपादस्य गृहे जातोउसि ध्रुव दुर्लभे
- **Translation**: 

---


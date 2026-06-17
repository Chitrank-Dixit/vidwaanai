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

### Verse 1 (Bhagwat Puran 0.8101)
- **Original**: भगवानने राजर्षि सत्यव्रतकों अपने स्वरूपके सम्पूर्ण रहस्यका वर्णन करते हुए ज्ञान, भक्ति और कर्मयोगसे परिपूर्ण दिव्य पुणणका उपदेश किया, जिसको 'मत्स्यपुराण' कहते हैं
- **Translation**: 

---

### Verse 2 (Bhagwat Puran 0.8102)
- **Original**: सत्यव्रतने ऋषियोंके साथ नावमें बैठे हुए हो सन्देहरहित होकर भगवानके द्वारा उपदिष्ट सनातन ब्रह्मस्वरूप आत्मतत्त्तका श्रवण किया
- **Translation**: 

---

### Verse 3 (Bhagwat Puran 0.8103)
- **Original**: इसके बाद जब पिछले प्रलयका अन्त हो गया और ब्रह्माजीकी नींद टूटी, तब भगवानने हयग्रीव असुर्को मारकर उससे वेद छोन लिये और ब्रह्माजीकों दे दिये
- **Translation**: 

---

### Verse 4 (Bhagwat Puran 0.8104)
- **Original**: भगवानकी कृपासे राजा सत्यव्रत ज्ञान और विज्ञानसे संयुक्त होकर इस कल्पमें वैवस्वत मनु हुए
- **Translation**: 

---

### Verse 5 (Bhagwat Puran 0.8105)
- **Original**: अपनी योगमायासे मत्््यरूप धारण करनेवाले भगवान्‌ विष्णु और राजर्पि सत्यव्रतका यह संबाद एवं श्रेष्ठ आख्यान सुनकर मनुष्य सब प्रकास्के पापोंसे मुक्त हो जाता है
- **Translation**: 

---

### Verse 6 (Bhagwat Puran 0.8106)
- **Original**: जो मनुष्य भगवानके इस अबतारका प्रतिदिन कोर्तन करता है, उसके सारे सड्ूल्प सिद्ध हो जाते हैं और उसे परमगतिकी प्राप्ति होती है
- **Translation**: 

---

### Verse 7 (Bhagwat Puran 0.8107)
- **Original**: प्रलयकालीन समुद्रमें जब ब्रह्माजी सो गये थे, उनकी सृष्टिशक्ति लुप्त हो चुकी थी , उस समय उनके मुखसे निकली हुई श्रुतियोंको चुराकर हयग्रीव दैत्य पातालमें ले गया था। भगवानने उसे मारकर ते श्रुतियाँ ब्रह्मजीकों लौटा दीं एवं सल्यत्रत तथा सप्तर्षियोंको ब्रह्मतत्वका उपदेश किया। उन समस्त जगत्‌के परम कारण लीलामत्य्य भगवान्‌कों मैं नमस्कार करता हूँ
- **Translation**: 

---

### Verse 8 (Bhagwat Puran 0.8108)
- **Original**: नानी + +-++
- **Translation**: 

---

### Verse 9 (Bhagwat Puran 0.8109)
- **Original**: इति अष्टम स्कन्ध समाप्त
- **Translation**: 

---

### Verse 10 (Bhagwat Puran 0.8110)
- **Original**: हरि: 3 तत्सतू
- **Translation**: 

---

### Verse 11 (Bhagwat Puran 0.8111)
- **Original**: । कीनन«मननकीननाणान अ+ %--ज +37ः+्
- **Translation**: 

---

### Verse 12 (Bhagwat Puran 0.8112)
- **Original**: प्रशधाकुषाध्यंचण....
- **Translation**: 

---

### Verse 13 (Bhagwat Puran 0.8113)
- **Original**: नमः श्रीमद्धागवतमहापुराण स रावणं लोकरावणम्‌। रामो भूत्वावधीद्यस्त॑ गोविन्द विन्दतां मनः
- **Translation**: 

---

### Verse 14 (Bhagwat Puran 0.8114)
- **Original**: 2 2] छः 2 052] ् 62] 18))
- **Translation**: 

---

### Verse 15 (Bhagwat Puran 0.8115)
- **Original**: 2] 2 24
- **Translation**: 

---

### Verse 16 (Bhagwat Puran 0.8116)
- **Original**: 462 562 *-
- **Translation**: 

---

### Verse 17 (Bhagwat Puran 0.8117)
- **Original**: रह श्छ । 2] 62] छ छ रह रे (82 62] (82 रे 62 र् 52
- **Translation**: 

---

### Verse 18 (Bhagwat Puran 0.8118)
- **Original**: ..-__-_->ह->-+ू--#-7+-ू-+++->->-8- 6-5
- **Translation**: 

---

### Verse 19 (Bhagwat Puran 0.8119)
- **Original**: 3 नमो भगवते वासुदेयाय श्रीमद्भागवतमहापुराण नाक 66538 नत्रम स्कन्ध पहला अध्याय खैबस्वत मनुके पुत्र राजा सुद्युम्नकी कथा राजा परीक्षितने पूछा--भगवन्‌ ! आपने सब मन्वन्‍्तरों और उनमें अनन्त शक्तिशाली भगबान्‌के द्वारा किये हुए ऐश्वर्यपूर्ण चरित्रोंक। वर्णन किया और मैंने उनका श्रवण भी किया
- **Translation**: 

---

### Verse 20 (Bhagwat Puran 0.8120)
- **Original**: आपने कहा कि पिछले कल्पके अन्तमें द्रविड़ देशके स्वामी राजर्पि सत्यत्नतने भगवानकी सेवासे ज्ञान प्राप्त किया और वहा इस कल्पमें वैवस्वत मनु हुए। आपने उनके इक्ष्वाकु आदि नरपति पुत्रोंका भो तर्णन किया
- **Translation**: 

---


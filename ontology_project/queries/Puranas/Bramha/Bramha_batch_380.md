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

### Verse 1 (Bramha 0.7581)
- **Original**: भयंकर दण्ड तत्काल ऊपर पड़ता है। जो शास्त्र- करना चाहिये और जिस प्रकार ब्राह्मणोंको संतोष
- **Translation**: 

---

### Verse 2 (Bramha 0.7582)
- **Original**: विधिकी अवहेलना करके मूर्खकों भोजन कराता हो, वैसी चेष्टा करनी चाहिये। अब मैँ श्राद्धमें
- **Translation**: 

---

### Verse 3 (Bramha 0.7583)
- **Original**: है, वह दाता प्राचीन धर्मका त्याग करनेके कारण त्याग देने योग्य अधम ब्राह्मणोंका वर्णन करता
- **Translation**: 

---

### Verse 4 (Bramha 0.7584)
- **Original**: नष्ट हो जाता है। जो अपने आश्रयमें रहनेवाले हूँ। मित्रद्रोही, खराब नखोंवाला, नपुंसक, क्षयका
- **Translation**: 

---

### Verse 5 (Bramha 0.7585)
- **Original**: ब्राह्मणका परित्याग करके दूसरेको बुलाकर भोजन रोगी, कोढ़ी, व्यापारी, काले दाँतोंवाला, गंजा,
- **Translation**: 

---

### Verse 6 (Bramha 0.7586)
- **Original**: कराता है, बह दाता उस ब्राह्मणके शोकोच्छवासकी काना, अंधा, बहरा, जड, गूँगा, पम्जु, हिजड़ा,
- **Translation**: 

---

### Verse 7 (Bramha 0.7587)
- **Original**: आगमें दग्ध होकर नष्ट हो जाता है। खराब चमड़ेवाला, हीनाक़, लाल आँखोंवाला,
- **Translation**: 

---

### Verse 8 (Bramha 0.7588)
- **Original**: वस्त्रके बिना कोई क्रिया, यज्ञ, वेदाध्ययन कुबड़ा, बौना, विकराल, आलसी, मित्रके प्रति
- **Translation**: 

---

### Verse 9 (Bramha 0.7589)
- **Original**: और तपस्या नहीं होती। अठ: श्राद्धकालमें वस्त्रका शत्रुभाव रखनेवाला, कलझ्वित कुलमें उत्पन्न, पशु
- **Translation**: 

---

### Verse 10 (Bramha 0.7590)
- **Original**: दान विशेष रूपसे करना चाहिये।* जो रेशमी, पालन करनेवाला, अच्छी आकृतिसे हीन, परिवित्ति
- **Translation**: 

---

### Verse 11 (Bramha 0.7591)
- **Original**: सूती और बिना कटा हुआ वस्त्र श्राद्धमें देता है, + शस्थाभावे क्रिया वास्ति यज्ञा येदास्तपांसि थ। तस्माद्वासांसि देयानि श्राद्धकाले विशेषत:
- **Translation**: 

---

### Verse 12 (Bramha 0.7592)
- **Original**: (220 139)
- **Translation**: 

---

### Verse 13 (Bramha 0.7593)
- **Original**: 366 * संक्षिप्त भ्रह्मपुराण * वह उत्तम भोगोंको प्राप्त करता है। जैसे बहुत-
- **Translation**: 

---

### Verse 14 (Bramha 0.7594)
- **Original**: आज्ञा ले ले; उसके बाद पिण्डोंको उठाये। अतः सी गौओंमें बछड़ा अपनी माताके पास पहुँच
- **Translation**: 

---

### Verse 15 (Bramha 0.7595)
- **Original**: ऋषियोंकी बतायी हुई विधिके अनुसार श्राद्धका जाता है, उसी प्रकार श्राद्धमें ब्राह्मणोंका भोजन
- **Translation**: 

---

### Verse 16 (Bramha 0.7596)
- **Original**: अनुष्ठान करे; अन्यथा दोष लगता है और पितरोंको किया हुआ अन्न जीवके पास, वह जहाँ भी रहता
- **Translation**: 

---

### Verse 17 (Bramha 0.7597)
- **Original**: भी नहीं मिलता। है, पहुँच जाता है। नाम, गोत्र और मन्त्र-ये
- **Translation**: 

---

### Verse 18 (Bramha 0.7598)
- **Original**: जौ, धान, तिल, गेहूँ, मूँग, सावाँ, सरसोंका अन्नको यहाँ ढोकर नहीं ले जाते, अपितु मृत्युको
- **Translation**: 

---

### Verse 19 (Bramha 0.7599)
- **Original**: तेल, तिन्नीका चावल और कैँगनी आदिसे पितरॉको प्राप्त हुए जीवॉतकको तृप्ति पहुँचती है--बे श्राद्धसे
- **Translation**: 

---

### Verse 20 (Bramha 0.7600)
- **Original**: तृप्त करे। आम, अमड़ा, बेल, अनार, बिजौरा, तृप्ति लाभ करते हैं। 'देवताभ्य: पितृभ्यश्च महायोगिभ्य
- **Translation**: 

---


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

### Verse 1 (Vaivtpuran 22.6979)
- **Original**: सामग्रीसे भगवती लक्ष्मीका पूजन किया और सिर भक्तिके कारण झुके हुए थे और अत्यन्त
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.6980)
- **Original**: देवताओंने उन्हें वन्य पदार्थोंका नैवेद्य समर्पित दीनतावश नेत्रोंमें आँसू छलक आये थे। उनके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.6981)
- **Original**: किया। फिर उन मुनीश्वरोंने हर्षक साथ उनकी ट्वारा कौ गयी स्तुतिको सुनकर सहस्नरदल-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.6982)
- **Original**: स्तुति करके भक्तिपूर्वक उनका आराधन किया कमलपर वास करनेवाली तथा सैकड़ों चन्द्रमाओंके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.6983)
- **Original**: और कहा--“जगदम्बिके! आप देवलोक तथा समान कान्तिमती महालक्ष्मी तुरंत ही वहाँ प्रकट
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.6984)
- **Original**: मर्त्लोकमें पधारिये।' उनका वह वचन सुनकर हो गयीं। मुने! उन जगन्माताकी उत्तम प्रभासे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.6985)
- **Original**: जगज्जननी संतुष्ट हो गयीं और ब्राह्मणोंकी आज्ञासे सारा जगत्‌ व्याप्त हो गया। तदनन्तर जगत्‌का
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.6986)
- **Original**: निर्भभ हो चलनेके लिये उद्यत होकर धारण-पोषण करनेवाली लक्ष्मीने देवताओंसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.6987)
- **Original**: उनसे बोलीं। यथोचित हितकारक एवं साररूप बचन कहा। श्रीमहालक्ष्मीने_ कहां--विप्रवरो! मैं श्रीमहालक्ष्मी बोलीं--बच्चो! तुमलोग
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.6988)
- **Original**: आपलोगोंकी आज्ञासे देवताओंके घर जाऊँगी, ब्रह्मशापके कारण भ्रष्ट हो गये हो, अत: मेरा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.6989)
- **Original**: किंतु भारतवर्षमें जिन-जिनके घर नहीं जाऊँगी, घर जानेका विचार नहीं है। इस समय
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.6990)
- **Original**: उनका विवरण सुनिये। पुण्यात्मा गृहस्थों और मैं ऐसा करनेमें समर्थ नहीं हूँ; क्योंकि मैं
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.6991)
- **Original**: उत्तम नीतिके जानकार नरेशोंके घरमें तो मैं ब्रह्मशापसे डर रही हूँ। ब्राह्मण मेरे प्राण हैं।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.6992)
- **Original**: स्थिररूपसे निवास करूँगी और पुत्रकी भाँति वे सभी सदा मुझे पुत्रसे भी बढ़कर प्रिय हैं।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.6993)
- **Original**: उनकी रक्षा करूँगी। जिस-जिसके प्रति उसके वे ब्राह्मण जो कुछ देते हैं, वही मेरी जीविकाका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.6994)
- **Original**: गुरु, देवता, माता, पिता, भाई-बन्धु, अतिथि और साधन होता है। यदि बे विप्र प्रसन्नतापूर्वक मुझसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.6995)
- **Original**: पितर लोग रुष्ट हो जायँगे, उसके घर मैं नहीं कहें तो मैं उनकी आज्ञासे चल सकूँगी। वे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.6996)
- **Original**: जाऊँगी। जो मिथ्यावादी, पराक्रमहीन और दुष्ट तपस्बी मेरी पूजा करनेमें समर्थ नहों हैं। जब
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.6997)
- **Original**: स्वभाववाला है तथा “मेरे पास कुछ नहीं है" अभाग्यका समय आ जाता है, तभी वे गुरु,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.6998)
- **Original**: यों सदा कहता रहता है, उसके घर मैं नहीं ब्राह्मण, देव, संन्यासी तथा वैष्णवोंद्वारा शापित
- **Translation**: 

---


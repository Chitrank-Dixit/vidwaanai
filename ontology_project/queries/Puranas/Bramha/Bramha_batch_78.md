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

### Verse 1 (Bramha 0.1541)
- **Original**: अन्य लोगोंकों विदा किया और स्वयं प्रमथगणोंके सृष्टिके कर्ता हैं, उन महादेवजीको प्रणाम है।
- **Translation**: 

---

### Verse 2 (Bramha 0.1542)
- **Original**: साथ अपने धामको चले गये। ब्राह्मणो! जो इस अनुग्रह करनेवाले भगवान्‌को नमस्कार है। पालन
- **Translation**: 

---

### Verse 3 (Bramha 0.1543)
- **Original**: स्तोश्नका श्रवण या पाठ करता है, वह सम्पूर्ण करनेवाले शिवको प्रणाम है। रुद्र, बसु, आदित्य ' लोकोंमें जानेकी शक्ति प्राप्त करता और देवराज और अश्विनीकुमारोंके रूपमें वर्तमान भगवान्‌
- **Translation**: 

---

### Verse 4 (Bramha 0.1544)
- **Original**: इन्द्रकी भाँति देवताओंद्वारा पूजित होता है। शड्भूरको नमस्कार है। जो सबके पिता, सांख्यवर्णित ,_ महादेवजी अपने धाममें प्रवेश करके जब पुरुष, विश्वेदेव, शर्व, उग्र, शिव, वरद, भीम,
- **Translation**: 

---

### Verse 5 (Bramha 0.1545)
- **Original**: सुन्दर आसनपर विण्जमान हुए, तब वक्र स्वभाववाले सेनानी, पशुपति, शुचि, वैरिहन्ता, सच्योजात, महादेव,
- **Translation**: 

---

### Verse 6 (Bramha 0.1546)
- **Original**: क्रूर कामदेबने उन्हें अपने बाणोंसे बींधनेका चित्र, विचित्र, प्रधान, अप्रमेय, कार्य और कारण
- **Translation**: 

---

### Verse 7 (Bramha 0.1547)
- **Original**: विचार किया। वह अनाचारी, दुय्रत्मा और कुलाधम नामसे प्रतिपादित होते हैं, उन भगवान्‌ शिवको
- **Translation**: 

---

### Verse 8 (Bramha 0.1548)
- **Original**: काम सब लोकोंको पीड़ित करनेवाला है। वह प्रणाम है। भगवन्‌! पुरुषरूपमें आपको नमस्कार
- **Translation**: 

---

### Verse 9 (Bramha 0.1549)
- **Original**: नियम तथा ब्रतोंका पालन करनेवाले ऋषियोंके है। पुरुषमें इच्छा उत्पन्न करनेवाले आपको प्रणाम
- **Translation**: 

---

### Verse 10 (Bramha 0.1550)
- **Original**: कार्यमें विन्न डाला करता है। उस दिन चक्रवाकका है। आप ही पुरुषका प्रकृतिके साथ संयोग कराते ' रूप धारण करके अपनी पत्नी रतिके साथ ठसका हैं और आप ही प्रकृतिमें गुणोंका आधान करनेवाले
- **Translation**: 

---

### Verse 11 (Bramha 0.1551)
- **Original**: आगमन हुआ था। देवताओंके स्वामी भगवान्‌ हैं। आपको नमस्कार है। आप प्रकृति और
- **Translation**: 

---

### Verse 12 (Bramha 0.1552)
- **Original**: शद्भूरने अपनेको बींधनेको इच्छा रखनेवाले आततायी पुरुषके प्रवर्तक, कार्य और कारणके विधायक
- **Translation**: 

---

### Verse 13 (Bramha 0.1553)
- **Original**: कामदेवको तीसरे नेत्रसे अवहेलनापूर्वक देखा। तथा कर्मफलोंकी प्राप्ति करानेबाले हैं। आपकी
- **Translation**: 

---

### Verse 14 (Bramha 0.1554)
- **Original**: फिर तो उनके नेत्रसे प्रकट हुई आग सहस(रों नमस्कार है। आप कालके ज्ञाता, सबके नियन्ता,
- **Translation**: 

---

### Verse 15 (Bramha 0.1555)
- **Original**: लपटोंके साथ प्रज्वलित हो ठठी और रतिके गुणोंकी विषमताके उत्पादक तथा प्रजावर्गको
- **Translation**: 

---

### Verse 16 (Bramha 0.1556)
- **Original**: स्वामी मदनकों उसके साज- श्रृज्ञारके साथ सहसा जीविका प्रदान करनेवाले हैं, आपको नमस्कार
- **Translation**: 

---

### Verse 17 (Bramha 0.1557)
- **Original**: दग्ध करने लगी। उस समय जलता हुआ कामदेव है। देवदेवेध्वर! आपको प्रणाम है। भूतभावन!
- **Translation**: 

---

### Verse 18 (Bramha 0.1558)
- **Original**: बड़े करुण स्वरमें आर्तनाद करने लगा और आपको नमस्कार है। कल्याणमय प्रभो! आप हमें
- **Translation**: 

---

### Verse 19 (Bramha 0.1559)
- **Original**: भगवान्‌ शिबको प्रसन्न करनेके लिये धरतीपर गिर दर्शन देनेके लिये प्रसन्‍त्रमुख एबं सौम्य हो जायें।
- **Translation**: 

---

### Verse 20 (Bramha 0.1560)
- **Original**: पड़ा। इतनेमें उसके सब अज्ञोंमें आग फैल गयी इस प्रकार देवताओंके द्वारा अपनी स्तुति
- **Translation**: 

---


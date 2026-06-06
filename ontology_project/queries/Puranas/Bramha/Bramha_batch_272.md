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

### Verse 1 (Bramha 0.5421)
- **Original**: स्थलमें श्रीवत्सका चिह्न सुशोभित था। हृदयदेश माहात्म्य सारसे भी अत्यन्त सारतर वस्तु है। वह
- **Translation**: 

---

### Verse 2 (Bramha 0.5422)
- **Original**: बनमालासे आवृत हो रहा था। मस्तकपर मुकुट इस पृथ्वीपर दुर्लभ है। विप्रगण! आदिकल्पकी
- **Translation**: 

---

### Verse 3 (Bramha 0.5423)
- **Original**: और भुजाओंमें अड्भद शोभा पाते थे। कंधे मोटे बात है, मैंने देवशिल्पियोंमें श्रेष्ठ विश्वकर्माकों जान पड़ते थे। कानोंमें कुण्डल झिलमिला रहे थे। बुलाकर कहा--' तुम पृथ्वीपर भगवान्‌ वासुदेवकी
- **Translation**: 

---

### Verse 4 (Bramha 0.5424)
- **Original**: श्याम अद्भपर पीताम्बरकी अपूर्व शोभा थी। इस शिलामयी प्रतिमा बनाओ, जिसका दर्शन करके
- **Translation**: 

---

### Verse 5 (Bramha 0.5425)
- **Original**: प्रकार वह प्रतिमा दिव्य थी। स्थापनाका समय इन्द्र आदि देवता और मनुष्य भक्तिपूर्वक भगवान्‌
- **Translation**: 

---

### Verse 6 (Bramha 0.5426)
- **Original**: आनेपर स्वयं मैंने ही गूढ़ मन्त्रोंद्वारा उसे स्थापित वासुदेवकी आराधना करें और उनकी कृपासे
- **Translation**: 

---

### Verse 7 (Bramha 0.5427)
- **Original**: उस समय देवराज इन्द्र ऐरावतपर सवार * गड्ला गड्ढेति यो ब्रूयाद्योजनानां शतैरपि। मुच्यते सर्वपापेभ्यो विष्णुलोक स गच्छति
- **Translation**: 

---

### Verse 8 (Bramha 0.5428)
- **Original**: तिख्र: कोट्यो5र्धकोटी च तीथांनि भुवनत्नये । तानि स्तातुं समायान्ति गड्जायां सिंहगे गुरौ
- **Translation**: 

---

### Verse 9 (Bramha 0.5429)
- **Original**: (175। 82-83) + चकार प्रत्िमां शुद्धां शबड्खचक्रगदाधराम्‌ू । सर्वलक्षणसंयुक्तां पुण्डरीकायते क्षणाम्‌। श्रीवत्सलक्ष्मसंयुक्तामत्युग्रां. प्रतिमोत्तमाम्‌
- **Translation**: 

---

### Verse 10 (Bramha 0.5430)
- **Original**: 262 * संक्षिप्त ब्रह्मपुराण « हो समस्त देवताओंके साथ मेरे लोकमें आये।
- **Translation**: 

---

### Verse 11 (Bramha 0.5431)
- **Original**: मुकुट, भुजाओंमें भुजबंध, हाथोंमें शड्ख, चक्र, उन्होंने स्नान-दान आदिके द्वारा भगवत्प्रतिमाको
- **Translation**: 

---

### Verse 12 (Bramha 0.5432)
- **Original**: गदा और पद्म, शरीरपर पीताम्बर, चार भुजाएं तथा प्रसन्न किया और उसे लेकर वे अपनी अमराबती
- **Translation**: 

---

### Verse 13 (Bramha 0.5433)
- **Original**: अज्जोंमें समस्त आभूषण शोभा दे रहे थे। बह पुरीमें चले गये। वहाँ इन्द्रभवनमें उसे पधराकर
- **Translation**: 

---

### Verse 14 (Bramha 0.5434)
- **Original**: प्रतिमा समस्त मनोबाब्छित फलोंको देनेवाली उन्होंने मन, वाणी और शरीरको संयममें रखते
- **Translation**: 

---

### Verse 15 (Bramha 0.5435)
- **Original**: थी। रावणने यहाँ रखे हुए ढेर-के-ढेर रत्रोंकों तो हुए दीर्घकालतक भगवान्‌की आराधना की और
- **Translation**: 

---

### Verse 16 (Bramha 0.5436)
- **Original**: छोड़ दिया और उस सुन्दर प्रतिमाकों तुरंत ही उन्हींके प्रसादसे वृत्र एवं नमुचि आदि क्रूर
- **Translation**: 

---

### Verse 17 (Bramha 0.5437)
- **Original**: पुष्पक बिमानसे लझ्ढमें भेज दिया। राक्षसों तथा भयंकर दानवोंका संहार करके तीनों
- **Translation**: 

---

### Verse 18 (Bramha 0.5438)
- **Original**: वहाँ रावणके छोटे भाई धर्मात्मा विभीषण लोकोंका राज्य भोगा। जगराध्यक्ष थे। वे सदा भगवान्‌ नारायणके भजनमें द्वितीय युग त्रेता आनेपर महापराक्रमी राक्षसराज
- **Translation**: 

---

### Verse 19 (Bramha 0.5439)
- **Original**: लगे रहते थे। देवराजकी भूमिसे आयी हुई उस रावण बड़ा प्रतापी हुआ। उसने दस हजार
- **Translation**: 

---

### Verse 20 (Bramha 0.5440)
- **Original**: दिव्य प्रतिमाको देखकर उनके शरीरमें रोमाझ् हो वर्षोतक निराहार और जितेन्द्रिय रहकर अत्यन्त
- **Translation**: 

---


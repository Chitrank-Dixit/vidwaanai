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

### Verse 1 (Vaivtpuran 13.10402)
- **Original**: डाली। इसके बाद श्रीकृष्ण पुष्पशब्यासे उठकर कौन कर सकता है? मैं, "महे श्वर और अनन्त कोई
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10403)
- **Original**: अग्निके समीप बैठे। फिर ब्रह्माजीकी बतायी हुई भी तुम्हारी स्तुति करनेकी क्षमता नहीं रखते।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10404)
- **Original**: विधिसे उन्होंने स्वयं हवन किया। तत्पश्चात्‌ सरस्वती और वेद भी अपनेको असमर्थ पाते हैं। श्रीकृष्ण और राधाको प्रणाम करके ब्रह्माजीने परमेश्वर! फिर कौन तुम्हारी स्तुति कर सकता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10405)
- **Original**: स्वयं पिताके कर्तव्यका पालन करते हुए उन है? मैंने आगमोंका अनुसरण करके तुम्हारे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10406)
- **Original**: दोनोंसे कौतुक (वैवाहिक मज्जल-कृत्य) कराये विषयमें जैसा कुछ कहा है, उसके लिये तुम
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10407)
- **Original**: और सात बार अग्निदेवकी परिक्रमा करवायी। मेरी निन्दा न करना। जो ईश्वरोंके भी ईश्वर इसके बाद राधासे अग्निकौ परिक्रमा करवाकर परमात्मा हैं, उनकी योग्य और अयोग्यपर भी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10408)
- **Original**: श्रीकृष्णको प्रणाम कराके राधाकों उनके पास समान कृपा होती है। जो पालनके योग्य संतान
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10409)
- **Original**: बैठाया। फिर श्रीकृष्णसे राधाका हाथ ग्रहण है, उसका क्षण-क्षणमें गुण-दोष प्रकट होता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10410)
- **Original**: कराया और माधवसे सात वैदिक मन्त्र पढ़वाये। रहता है; परंतु माता और पिता उसके सारे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10411)
- **Original**: तत्पश्चात्‌ बेदज्ञ विधाताने श्रीहरिके वक्ष:स्थलपर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10412)
- **Original**: 5 श्रीकृष्णजन्मखण्ड * 467 ##ऋ## # # कक ऋकऋ्क््ऋ्ऋऋऋऋऋऋऋऋऋऋऋऋऋऋऋऋक्ऋ्ऋझ## ######&######## 5 ### राधिकाका हाथ रखवाकर राधाके पृष्ठदेशमें श्रीकृष्णका
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10413)
- **Original**: सर्वांड़ु पुलकित हो उठा था। वे प्रेमबेदनाका हाथ रखवाया और राधासे तीन वैदिक मन्त्रोंका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10414)
- **Original**: अनुभव कर रही थीं। श्रीहरिको भक्तिभावसे पाठ करवाया। तदनन्तर ब्रह्माने पारिजातके पुष्पोंकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10415)
- **Original**: प्रणाम करके श्रीराधा उनकी शब्यापर गयीं। वहाँ आजानुलम्बिनी माला श्रीराधाके हाथसे श्रीकृष्णके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10416)
- **Original**: चन्दन, अगुरु, कस्तूरी और केसरका अड्भराग गलेमें डलवायी। तत्पश्चात्‌ कमलजन्मा विधाताने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10417)
- **Original**: रखा हुआ था। श्रीराधाने श्रीकृष्णके ललारमें पुन: श्रीराधा और श्रीकृष्णको प्रणाम करके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10418)
- **Original**: तिलक करके उनके वक्ष:स्थलमें चन्दन लगाया। श्रीहरिके हाथसे श्रीराधाके कण्ठमें मनोहर माला
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10419)
- **Original**: फिर सुधा और मधुसे भरा हुआ मनोहर रत्लपात्र डलबायी। फिर श्रीकृष्णको बैठाया और उनके
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10420)
- **Original**: भक्तिपूर्वक श्रीहरिके हाथमें दिया। जगदीश्वर वामपार्श्वमें मन्द-मन्द मुस्कराती हुई श्रीकृष्णहदया श्रोकृष्णने उस सुधाका पान किया। इसके बाद राधाको भी बैठाया। इसके बाद उन दोनोंसे हाथ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10421)
- **Original**: श्रीराधाने कर्पूर आदिसे सुवासित सुरम्य ताम्बूल जुड़वाकर पाँच वैदिक मन्त्र पढ़वाये। तत्पश्चात्‌ श्रीकृष्णो दिया। श्रीहरिने उसे सादर भोग विधाताने पुनः श्रीकृष्णकों प्रणाम करके, जैसे [लगाया। फिर श्रीहरिके दिये हुए सुधारसका पिता अपनी पुत्रीका दान करता है, उसी प्रकार
- **Translation**: 

---


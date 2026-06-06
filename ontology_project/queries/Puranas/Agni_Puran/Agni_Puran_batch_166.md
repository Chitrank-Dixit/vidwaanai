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

### Verse 1 (Agni Puran 0.3301)
- **Original**: नहीं रहता। जो मृत्युसे ग्रस्त है, उसे औषध और बाद करना है, उसे पहले ही पहरमें कर ले;
- **Translation**: 

---

### Verse 2 (Agni Puran 0.3302)
- **Original**: मन्त्र आदि नहीं बचा सकते। जैसे बछड़ा गौओंके क्योंकि मृत्यु इस बातकी प्रतीक्षा नहीं करती कि
- **Translation**: 

---

### Verse 3 (Agni Puran 0.3303)
- **Original**: झुंडमें भी अपनी माँके पास पहुँच जाता है, उसी इसका कार्य पूरा हो गया है या नहीं? मनुष्य
- **Translation**: 

---

### Verse 4 (Agni Puran 0.3304)
- **Original**: प्रकार पूर्वजन्मका किया हुआ कर्म जन्मान्तरमें भी खेत-बारी, बाजार-हाट तथा घर-द्वारमें फँसा
- **Translation**: 

---

### Verse 5 (Agni Puran 0.3305)
- **Original**: कर्ताकों अवश्य ही प्राप्त होता है। इस जगत्‌का होता है, उसका मन अन्यत्र लगा होता है; इसी
- **Translation**: 

---

### Verse 6 (Agni Puran 0.3306)
- **Original**: आदि और अन्त अव्यक्त है, केबल मध्यकी दशामें जैसे असावधान भेड़को सहसा भेड़िया
- **Translation**: 

---

### Verse 7 (Agni Puran 0.3307)
- **Original**: अवस्था ही व्यक्त होती है। जैसे जीवके इस शरीरमें आकर उठा ले जाय, वैसे ही मृत्यु उसे लेकर
- **Translation**: 

---

### Verse 8 (Agni Puran 0.3308)
- **Original**: कुमार तथा यौवन आदि अवस्थाएँ क्रमश: आती चल देतों है। कालके लिये न तो कोई प्रिय है,
- **Translation**: 

---

### Verse 9 (Agni Puran 0.3309)
- **Original**: रहती हैं, उसी प्रकार मृत्युके पश्चात्‌ उसे दूसरे न द्वेषका पात्र*
- **Translation**: 

---

### Verse 10 (Agni Puran 0.3310)
- **Original**: शरीरकी भी प्राप्ति होती है। जैसे मनुष्य (पुराने आयुष्य तथा प्रारब्धकर्म क्षीण होनेपर वह
- **Translation**: 

---

### Verse 11 (Agni Puran 0.3311)
- **Original**: बस्त्रको त्यागकर) दूसरे नूतन वस्त्रको धारण हठात्‌ जीवकों हर ले जाता है। जिसका काल
- **Translation**: 

---

### Verse 12 (Agni Puran 0.3312)
- **Original**: करता है, उसी प्रकार जीव एक शरीरकों छोड़कर नहीं आया है, वह सैकड़ों बाणोंसे घायल होनेपर
- **Translation**: 

---

### Verse 13 (Agni Puran 0.3313)
- **Original**: दूसरेको ग्रहण करता है। देहधारी जीवात्मा सदा भी नहीं मरता तथा जिसका काल आ पहुँचा है,
- **Translation**: 

---

### Verse 14 (Agni Puran 0.3314)
- **Original**: अवध्य है, वह कभी मरता नहीं; अतः मृत्युके बह कुशके अग्रभागसे ही छू जाय तो भी जीवित
- **Translation**: 

---

### Verse 15 (Agni Puran 0.3315)
- **Original**: लिये शोक त्याग देना चाहिये
- **Translation**: 

---

### Verse 16 (Agni Puran 0.3316)
- **Original**: 11--14
- **Translation**: 

---

### Verse 17 (Agni Puran 0.3317)
- **Original**: इस ग्रकार आदि आस्नेव महापुराणमें 'अम्ल॑स्कृत आदिको जुद्धिका वर्णव” वामक एक साँ उनसठवाँ अध्याय यूरा हुआ
- **Translation**: 

---

### Verse 18 (Agni Puran 0.3318)
- **Original**: 159 # एक सौ साठवाँ अध्याय वानप्रस्थ-आशभ्रम पुष्कर कहते हैं-- अब मैं वानप्रस्थ और
- **Translation**: 

---

### Verse 19 (Agni Puran 0.3319)
- **Original**: गृहस्थ पुरुषको उचित है कि अपनी संतानकी संन्यासियोंके धर्मका जैसा वर्णन करता हूँ, सुनो ।
- **Translation**: 

---

### Verse 20 (Agni Puran 0.3320)
- **Original**: संतान देखकर वनका आश्रय ले और आयुका सिरपर' जटा रखना, प्रतिदित अग्निहोत्र करना,
- **Translation**: 

---


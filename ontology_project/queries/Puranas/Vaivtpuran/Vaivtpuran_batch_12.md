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

### Verse 1 (Vaivtpuran 0.421)
- **Original**: मन्त्र आदिका उत्तम उपदेश देकर विधाताके भी विधिपूर्वक ध्यानका उपदेश दिया तथा भक्तोंपर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 0.422)
- **Original**: विधाता भगवान्‌ श्रीकृष्ण सृष्टिके लिये ब्रह्माजीसे अआनुग्रह करनेके लिये श्री (श्रीं), माया (हीं)
- **Translation**: 

---

### Verse 3 (Vaivtpuran 0.423)
- **Original**: इस प्रकार बोले-- तथा काम (क्लीं) बीजसहित दशाक्षर-मन्त्रका श्रीभगवान्‌ने कहा--महाभाग विधे! तुम उपदेश दिया। साथ ही सृष्टिके लिये उपयोगी
- **Translation**: 

---

### Verse 4 (Vaivtpuran 0.424)
- **Original**: सहस्र दिव्य बर्षोतक मेरी प्रसन्नताके लिये तप शक्ति और मनोबाञिछत वस्तु प्रदान करनेबाली
- **Translation**: 

---

### Verse 5 (Vaivtpuran 0.425)
- **Original**: करके नाना प्रकारकी उत्तम सृष्टि करो। सम्पूर्ण सिद्धि देकर भगवानने प्रकृतिको उत्कृष्ट... ऐसा कहकर श्रीकृष्णने ब्रह्माजीको एक मनोरम तत्त्वज्ञान भी प्रदान किया। इस तरह उसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 0.426)
- **Original**: माला दी। फिर गोप-गोपियोंके साथ बे नित्य-नूतन त्रयोदशाक्षर-मन्त्र देकर जगदीश्वर श्रीकृष्णने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 0.427)
- **Original**: दिव्य वृन्दाबनमें चले गये। (अध्याय 6) शी >;रसपियएब->>>> सृष्टिका क्रम--ब्रह्माजीके द्वारा मेदिनी, पर्वत, समुद्र, द्वीप, मर्यादापर्वत, पाताल, स्वर्ग आदिका निर्माण; कृत्रिम जगत्‌की अनित्यता तथा बैकुण्ठ, शिवलोक तथा गोलोककी नित्यताका प्रतिपादन सौति कहते हैं--शौनकजी ! तब भगवान्‌की
- **Translation**: 

---

### Verse 8 (Vaivtpuran 0.428)
- **Original**: हैं। इन समुद्रोंसे घिरे हुए सात द्वीप हैं। उनके आज्ञाके अनुसार तपस्या करके अभीष्ट सिद्धि
- **Translation**: 

---

### Verse 9 (Vaivtpuran 0.429)
- **Original**: भूमण्डल कमलपत्रकी आकृतिवाले हैं। उनमें पाकर ब्रह्माजीने सर्वप्रथम मधु और कैटभके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 0.430)
- **Original**: उपद्वीप और मर्यादापर्वत भी सात-सात ही हैं। मेदेसे मेदिनीकी सृष्टि की। उन्होंने आठ प्रधान
- **Translation**: 

---

### Verse 11 (Vaivtpuran 0.431)
- **Original**: ब्रह्मन्‌! अब आप उन ट्वीपोंके नाम सुनिये, पर्वतोंकी रचना की। वे सब बड़े मनोहर थे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 0.432)
- **Original**: जिनकी पहले ब्रह्माजीनी रचना की थी। वे उनके बनाये हुए छोटे-छोटे पर्वत तो असंख्य
- **Translation**: 

---

### Verse 13 (Vaivtpuran 0.433)
- **Original**: हैं--जम्बूद्वीप, शाकट्ठीप, कुशद्वीप, प्लक्षद्वीप, हैं, उनके नाम कया बताऊँ? मुख्य-मुख्य पर्वतोंकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 0.434)
- **Original**: क्रौद्वीप, न्यग्रोध (अथवा शाल्मलि)-द्वीप तथा नामावली सुनिये-सुमेरु, कैलास, मलय, हिमालय,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 0.435)
- **Original**: पुष्करद्दीप। भगवान्‌ ब्रह्माने मेरुपर्वतके आठ उदयाचल, अस्ताचल, सुबेल और गन्धमादन--ये
- **Translation**: 

---

### Verse 16 (Vaivtpuran 0.436)
- **Original**: शिखरोंपर आठ लोकपालोंके बिहारके लिये आठ आठ प्रधान पर्वत हैं। फिर ब्रह्माजीने सात समुद्रों, मनोहर पुरियोंका निर्माण किया। उस पर्वतके अनेकानेक नदों और कितनी ही नदियोंकी सृष्टि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 0.437)
- **Original**: मूलभाग-पाताललोकमें उन्होंने भगवान्‌ अनन्त की। वृक्षों, गाँवों और नगरोंका निर्माण किया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 0.438)
- **Original**: (शेषनाग)-की नगरी बनायी। तदनन्तर लोकनाथ समुद्रोंक नाम सुनिये--लवण, इक्षुरस, सुरा, घृत,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 0.439)
- **Original**: ब्रह्मेने उस पर्बतके ऊपर-ऊपर सात स्वर्गोंकी दही, दूध और सुस्वादु जलके वे समुद्र हैं।[सृष्टि की। शौनकजी! उन सबके नाम उनमेंसे पहलेकी लंगब्राई-चौड़ाई एक लाख
- **Translation**: 

---

### Verse 20 (Vaivtpuran 0.440)
- **Original**: सुनिये- भूलोंक , भुवलोंक, परम मनोहर स्वर्लोक, योजनकी है। बादवाले उत्तरोत्तर दुगुनें होते गये
- **Translation**: 

---


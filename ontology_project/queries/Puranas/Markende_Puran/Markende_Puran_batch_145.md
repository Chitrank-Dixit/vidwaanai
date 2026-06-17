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

### Verse 1 (Markende Puran 0.2881)
- **Original**: + घूप्रलोचन-यध + 219
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2882)
- **Original**: 65 5555 555 है 65 है 6 € 6 #65%5#: बष्ठोउ ध्याय: धूप्रलोचन-वध ध्यान पकड़कर घसीटते हुए जबरदस्ती यहाँ ले ( 3» नागाधी श्वरविष्टरां फणिफणोत्तंसोरुरलाबली-
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2883)
- **Original**: उसकी रक्षा करनेके लिये यदि कोई भास्वद्देहलतां दिवाकरनिभां नेत्रत्रयोद्धासिताम्‌। मालाकुम्भकपालनीरजकरां. चन्द्रार्थचूडां परां सर्वज्ञेश्वरभैरवाड्डुनिलयां पद्मावती चिन्तये
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2884)
- **Original**: मैं सर्वज्ञेश्वर भैरवके अड्डूमें निवास करनेबाली परमोत्कृष्ट पद्मावती देवीका चिन्तन करता हूँ। वे नागराजके आसनपर बैठी हैं, नागोंके फणोंमें सुशोभित होनेवाली मणियोंकी बिशाल मालासे उनकी देहलता उद्धासित हो रही है। सूर्यके समान उनका तेज है, तीन नेत्र उनकी शोभा बढ़ा रहे हैं। वे हाथोंमें माला, कुम्भ, कपाल और कमल लिये हुए हैं तथा उनके मस्तकमें अर्द्धचन्रका मुकुट सुशोभित है।) ऋषिरुवाच
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2885)
- **Original**: ' 37 इत्याकर्ण्य बच्चो देव्या: स दूतो3मर्षपूरित:। समाचष्ट समागम्य दैत्यराजाय विस्तरातू
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2886)
- **Original**: तस्य दूतस्य तद्वाक्यमाकर्ण्यासुरराद्‌ ततः। सक्रोध: प्राह दैत्यानामधिपं धूप्रलोचनम्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2887)
- **Original**: है धूप्रलोचनाशु त्वं स्वसैन्यपरिवारित:। तामानय बलाद्‌ दुष्टां केशाकर्षणविद्लाम्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2888)
- **Original**: तत्परिन्नाणद: कश्चिद्यदि वोत्तिप्ठतेउपर:। स॑ हन्तव्योउमरो बापि यक्षो गन्धर्व एव बा
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2889)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2890)
- **Original**: देवोका यह कथन सुनकर दूतकों बड़ा अमर्ष हुआ और उसने दैत्ययाजके पास जाकर सब समाचार विस्तारपूर्वक कह सुनाया
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2891)
- **Original**: दूतके उस बचनको सुनकर दैत्यगज कुपित हो उठा और दैत्यसेनापति धूम्नलोचनसे बोला-
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2892)
- **Original**: 'धूम्नलोचन ! तुम शौघ्र अपनी सेना साथ लेकर जाओं और उस दुष्टाको केश दूसरा खड़ा हो तो वह देवता, यक्ष अथवा गन्धर्व-कोई भी क्‍यों न हो, उसे अवश्य मार डालना'
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2893)
- **Original**: तेनाज्ञमस्ततः शीघ्र सर दैत्यो धूप्रलोचन:। बृतः षष्टया सहस्त्राणामसुराणां द्ुतं ययौ
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2894)
- **Original**: स दृष्टा तां ततो देवीं तुहिनाचलसंस्थिताम्‌। जगादोच्चै: प्रयाहीति मूल शुम्भनिशुम्भयो:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2895)
- **Original**: न॒चेत्प्रीत्याद्य भवती मद्धर्तारमुपैष्यति। ततो बलान्नयाम्येष केशाकर्षणविद्धलाम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2896)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2897)
- **Original**: शुम्भके इस प्रकार आज्ञा देनेपर बह धूग्नलोचन दैत्य स्राठ हजार असुरोंकी सेनाको साथ लेकर बहाँसे तुरंत चल
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2898)
- **Original**: 2152 » स्रेक्षित मार्काडेबपुराण 6045204444:1:4 # # 60560 व3.3फ# 4 2444 +शश:पऔफ रस * 0 वजह अ 4 485 » 07 श5ह 228 कर 2 44 7 230 >ज::फ.4 डक + दिय।
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2899)
- **Original**: वहाँ पहुँचकर उसने हिपाज्यपर असुर धूप्लोचन उनकी ओर दौड़ा, तब अम्बिकाने 'रहनेवाली उन देवीकों देखा और ललकारकर
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2900)
- **Original**: हुं” शब्दके उच्चारणमात्रसे उसको भस्म कर कहा--अरो! तू शुभ्म-गिशुप्थके फाप्त चल।।
- **Translation**: 

---


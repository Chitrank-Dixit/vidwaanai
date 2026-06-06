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

### Verse 1 (Rig Ved 0.10981)
- **Original**: 4777, नयसीद्वति द्विष: कृणोष्युक्थशंसिन: । नृभि: सुवीर उच्यसे
- **Translation**: 

---

### Verse 2 (Rig Ved 0.10982)
- **Original**: है इन्रदेव ! आप हमारे शत्रुओं को हमसे दूर भगाते हैं। हम आपको प्रशंसा करते हैं। आप श्रेष्ठ वोर कहलाते हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.10983)
- **Original**: 4778. ब्रह्माणं ब्रह्मवाहसं गीर्भि: सखायमृग्मियम्‌। गां न दोहसे हुवे
- **Translation**: 

---

### Verse 4 (Rig Ved 0.10984)
- **Original**: इद्धदेव ज्ञानी हैं, अतः ज्ञायपूर्वक स्तुत्य हैं । वे मित्र हैं; प्रशंसा के योग्य हैं, ऐसे इद्धदेव को हम स्तुति करके वैसे ही बुलाते हैं, जैसे दोहन के लिए गौओं को बुलाया जाता है
- **Translation**: 

---

### Verse 5 (Rig Ved 0.10985)
- **Original**: 4779. यस्य विश्वानि हस्तयोरूचुर्वसूनि नि द्विता
- **Translation**: 

---

### Verse 6 (Rig Ved 0.10986)
- **Original**: वीरस्य पृतनापह:
- **Translation**: 

---

### Verse 7 (Rig Ved 0.10987)
- **Original**: शत्रुओं को पराजित करने वाले इन्धदेव के दोनों हाथों में दोनों प्रकार को (दिव्य एवं पार्थिव सम्पत्तियाँ) हैँ, ऐसा क्रुषियों ने कहा है
- **Translation**: 

---

### Verse 8 (Rig Ved 0.10988)
- **Original**: 4780, वि दृब्व्हानि चिदद्विवों जनानां शचीपते
- **Translation**: 

---

### Verse 9 (Rig Ved 0.10989)
- **Original**: वृह माया अनानत
- **Translation**: 

---

### Verse 10 (Rig Ved 0.10990)
- **Original**: हे बच्रधारी इन्द्रदेव ! आप सर्वशक्तिमान्‌ हैं । आप शत्रुओं के किलों, नगरों एवं बलों को ध्वस्त करने वाले हैं। हे अनानत्‌ (न झुकने वाले) इद्रदेव ! आप उनकी माया को नष्ट करें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.10991)
- **Original**: 47831. तमु त्वा सत्य सोमपा इन्द्र वाजानां पते
- **Translation**: 

---

### Verse 12 (Rig Ved 0.10992)
- **Original**: अहूमहि श्रवस्थव:
- **Translation**: 

---

### Verse 13 (Rig Ved 0.10993)
- **Original**: हे सोमरस पीकर आनन्दित हुए इन्द्रदेव ! हम अन्न प्राप्ति को इच्छा से आपका आवाहन करते हैं
- **Translation**: 

---

### Verse 14 (Rig Ved 0.10994)
- **Original**: 4782. तमु त्वा यः पुरासिथ यो वा नूनं हिते धने। हव्य: स श्रुधी हवम्‌
- **Translation**: 

---

### Verse 15 (Rig Ved 0.10995)
- **Original**: युद्ध में सहायता के लिए प्राचोनकाल में आपको ही बुलाया गया था, भविष्य में भी आपको ही बुलाया जायेगा । जो संग्राम के समय बुलाए जाते हैं। जिनकी सहायता से शत्रु द्वारा धन प्राप्त होतां है । उन इन्द्रदेव को हम बुलाते हैं । वे हमारे आवाहन को सुनें
- **Translation**: 

---

### Verse 16 (Rig Ved 0.10996)
- **Original**: 4783. धीभिरव॑द्धिर्वतो वाजाँ इन्द्र श्रवाय्यान्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.10997)
- **Original**: त्वया जेष्म हितं धनम्‌
- **Translation**: 

---

### Verse 18 (Rig Ved 0.10998)
- **Original**: हे इद्धदेव !आप हमारी स्तुति से प्रसन्न हों । हम आपके अनुकूल होकर, शत्रु को जोतकर धन प्राप्त करें
- **Translation**: 

---

### Verse 19 (Rig Ved 0.10999)
- **Original**: 4784. अभूरु वीर गिर्वणो महाँ इन्द्र धने हिते । भरे वितन्तसाय्य:
- **Translation**: 

---

### Verse 20 (Rig Ved 0.11000)
- **Original**: हे इन्द्रदेव !आप वीर एवं स्तुति के योग्य हैं । आपने शत्रुओं के धन को प्राप्त करने के लिए उन्हें जीता
- **Translation**: 

---


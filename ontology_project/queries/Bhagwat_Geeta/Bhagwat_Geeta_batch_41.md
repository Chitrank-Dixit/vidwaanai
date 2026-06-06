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

### Verse 1 (Bhagwat_Geeta 10.959)
- **Original**: । मैं छल करनेवालोंमें जूआ और प्रभावशाली पुरुषोंका प्रभाव हूँ। मैं जीतनेवालोंका विजय हूँ, निश्चय करनेवालोंका निश्चय और सात्त्विक पुरुषोंका सात्त्विक भाव हूँ
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 10.960)
- **Original**: वृष्णीनां वासुदेवो5स्मि पाण्डवानां धनज्जयः । मुनीनामप्यहं व्यास: कवीनामुशना कवि:
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 10.961)
- **Original**: वृष्णिवंशियोंमें वासुदेव अर्थात्‌ मैं स्वयं तेरा सखा, पाण्डवोंमें धनझय अर्थात्‌ तू, मुनियोंमें वेदव्यास और 1. कीर्ति आदि ये सात देवताओंकी स्त्रियाँ और स्त्री-वाचक नामवाले गुण भी प्रसिद्ध हैं, इसलिये दोनों प्रकारसे ही भगवान्‌की विभूतियाँ हैं। 2. यादवोंके ही अन्तर्गत एक वृष्णिवंश भी था।
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 10.962)
- **Original**: * अध्याय 10* 139 कवियोंमें शुक्राचार्य कवि भी मैं ही हूँ
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 10.963)
- **Original**: दण्डो दमयतामस्मि नीतिरस्मि जिगीषताम्‌। मौन चैवास्मि गुद्यानां ज्ञानं ज्ञानवतामहम्‌
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 10.964)
- **Original**: मैं दमन करनेवालोंका दण्ड अर्थात्‌ दमन करनेकी शक्ति हूँ, जीतनेकी इच्छावालोंकी नीति हूँ, गुप्त रखनेयोग्य भावोंका रक्षक मौन हूँ और ज्ञानवानोंका तत्त्वज्ञान मैं ही हूँ
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 10.965)
- **Original**: यच्चापि सर्वभूतानां बीज॑ तदहमर्जुन। न तदस्ति विना यत्स्यान्मया भूतं चराचरम्‌
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 10.966)
- **Original**: । और हे अर्जुन ! जो सब भूतोंकी उत्पत्तिका कारण है, वह भी मैं ही हूँ; क्योंकि ऐसा चर और अचर कोई भी भूत नहीं है, जो मुझसे रहित हो
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 10.967)
- **Original**: नान्तो5स्ति मम दिव्यानां विभूतीनां परन्तप। एप तूददेशतः प्रोक्तो विभूतेर्विस्तरो मया
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 10.968)
- **Original**: हे परंतप ! मेरी दिव्य विभूतियोंका अन्त नहीं है, मैंने अपनी विभूतियोंका यह विस्तार तो तेरे लिये एकदेशसे अर्थात्‌ संक्षेपसे कहा है
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 10.969)
- **Original**: यद्यद्विभूतिमत्सत्त्वं श्रीमदूर्जितमेव॒ वा। तत्तदेवावगच्छ त्वं मम तेजों शसम्भवम्‌
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 10.970)
- **Original**: जो-जो भी विशभूतियुक्त अर्थात्‌ ऐश्वर्ययुक्त,
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 10.971)
- **Original**: 140 * श्रीमद्धगवद्रीता * कान्तियुक्त और शक्तियुक्त वस्तु है, उस-उसको तू मेरे तेजके अंशकी ही अभिव्यक्ति जान
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 10.972)
- **Original**: अथवा बहुनैतेन किं ज्ञातेन तवार्जुन। विष्टभ्याहमिदं कृत्स्नमेकांशेन स्थितो जगत्‌
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 10.973)
- **Original**: अथवा हे अर्जुन! इस बहुत जाननेसे तेरा क्‍या प्रयोजन है। मैं इस सम्पूर्ण जगत्‌को अपनी योगशक्तिके एक अंशमात्रसे धारण करके स्थित हूँ
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 10.974)
- **Original**: 3» तत्सदिति श्रीमद्धगवद्गीतासूपनिषत्सु ब्रह्मविद्यायां योगशास्त्रे श्रीकृष्णार्जुनसंवादे विभूतियोगो नाम दशमोऊ ध्याय:
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 10.975)
- **Original**: अधैकादशो5 ध्याय: अर्जुन उवाच मदनुग्रहाय परमं गुह्ामध्यात्मसडिज्ञतम्‌ । यत्त्वयोक्ते वचस्तेन मोहो5यं विगतो मम
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 10.976)
- **Original**: अर्जुन बोले--मुझपर अनुग्रह करनेके लिये आपने जो परम गोपनीय अध्यात्मविषयक वचन अर्थात्‌ उपदेश कहा, उससे मेरा यह अज्ञान नष्ट हो गया है
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 10.977)
- **Original**: भवाप्ययौ हि भूतानां श्रुतौ विस्तरशो मया। त्वत्त: कमलपपत्राक्ष माहात्म्यमपि चाव्ययम्‌
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 10.978)
- **Original**: क्योंकि हे कमलनेत्र ! मैंने आपसे भूतोंकी उत्पत्ति
- **Translation**: 

---


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

### Verse 1 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.21)
- **Original**: 4।। यह मंत्र पढ़कर अपने इष्टदेवता को स्मरण करते हुए जल सहित कुशा से अपने आपको, स्त्री को तथा पूजा की सामग्री को पवित्र करे। पश्चात्‌ हाथ में पुष्पाक्षत लेकर 'ड0 आधारशक्तये नमः, ऊँ? कूर्माय नमः, ऊँ. अनन्ताय नमः, ऊँ पृथिव्यै नम” ऐसा कहकर चारों ओर अक्षत छिड़के । तत्पश्चातु श्वेत सरसों लेकर दिग्बन्धन” करे। यथा-- “पूर्वे रक्षतु वाराह आग्नेय्यां गरुडध्वजः
- **Translation**: 

---

### Verse 2 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.22)
- **Original**: दक्षिणे पद्मनाभस्तु नैकत्यां मघुसूदनः 1 पश्टचिमे चैव गोविन्दो वायव्यां तु जनार्दन: । उत्तेर श्रीपति: रक्षेदशान्यां तु महेश्वर:
- **Translation**: 

---

### Verse 3 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.23)
- **Original**: ऊर्ध्व रक्षतु धाताव्जी अधोडनन्तश्व रक्षतु । अनुक्तामपि यत्स्थानें रक्षत्वी शो ममादिधृका।3
- **Translation**: 

---

### Verse 4 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.24)
- **Original**: ह 8 श्री विश्वकर्मा पुराण एवं पूजन पद्धति
- **Translation**: 

---

### Verse 5 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.25)
- **Original**: अपसर्पन्तु ते भूता ये भूता भूमि संस्थिताः । ये भूता विस्नकत्तारस्ते नश्यन्तु शिवाज्ञया
- **Translation**: 

---

### Verse 6 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.26)
- **Original**: तत्पश्चात्‌ दूरवाक्षतगन्धपुष्पाणि जलपात्रे निधाय धेनुमुद्रया अमृतीकरणं मत्स्यमुद्रया5ज्च्छादनश्ल कृत्वा अंकुशमुद्रया जले तीर्थावाहनं कुर्यात्‌ । यथा- दिग्बन्धन करने के बाद रक्षासूत्र पुरुष के दाहिने हाथ में और स्त्री के वायें हाथ में बांधकर दूर्वाक्षत, पुष्प, जल पात्र में छोड़े । तत्पश्चात्‌ धेनु मुद्रा से अमृतीकरण मत्स्य मुद्रा से ढंककर, अंकुश मुद्रा से जल में तीर्थों का आवाहन करें- ऊँ गन्ने च॒ यमुने चैव गोदावरि सरस्वति। नर्मदे सिन्धु कावेरि ! जलेडस्मिनू सन्नि्धि कुरु
- **Translation**: 

---

### Verse 7 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.27)
- **Original**: ततः स्वहदये विश्वकर्माणं ध्यात्वा, रक्षादीपं प्रज्वाल्य, गन्धाक्षतपुष्पाणि गृहीत्वा स्वस्तिवाचनं कुयत्त्‌ । इसके बाद अपने हृदय में विश्वकर्मा भगवान का ध्यान करे और रक्षादीप जलावे । फिंर हाथ में गन्धाक्षत पुष्प लेकर स्वस्तिवाचन (वैदिक मज़्ल मन्त्र पढ़कर) करे। तन्र विश्वकर्मा ध्यान मन्त्र यथा- “ऊँ विश्वकर्मनू हविषा वावृधानः स्वयं यजस्व प्रथिवीमुत घामू। महान्त्वन्येडअभिश&् सपत्ना इहाउस्माक॑ माघवा. सूरिस्स्तु
- **Translation**: 

---

### Verse 8 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.28)
- **Original**: ”” इसके बाद निम्नलिखित वैदिक मन्त्रों से स्वस्तिवाचन करना चाहिए । जैसे- ऊँ हरि: । ऊँ स्वस्ति न इन्द्रो वृद्धश्रवाः: स्वस्ति ना पूषा विश्ववेदाः । स्वस्ति नस्ताक्ष्यों अअरिष्टनेमि: स्वस्ति नो बृहस्पतिर्दघातु
- **Translation**: 

---

### Verse 9 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.29)
- **Original**: ऊँ पृषदश्वा सरुतः पूश्निमातरः शुभं य्यवानो व्विदधेषु जग्मयः । अग्निर्जिहा मनव: सूरचक्षसो व्विश्वे नो देवाघअवसागमन्िह
- **Translation**: 

---

### Verse 10 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.30)
- **Original**: ऊँ भद्ं कर्णभिः श्यूणुयाम देवा भद्-ं पश्वेमाक्भियजन्ना: । स्थिरैरंगेस्तुष्ट्वाथ्ड सस्तनूभिर्व्यशेमहि देवहितं यदायुः
- **Translation**: 

---

### Verse 11 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.31)
- **Original**: शतमिन्नु शरदोउअन्ति देवा यत्रा नश्चक्रा जरसन्तनूनामू । पुत्रासो यत्र पितरो मवन्ति मा नो मध्या रीरिषतायुर्गन्तोः:
- **Translation**: 

---

### Verse 12 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.32)
- **Original**: अदिति्धोरदितिरन्तरिक्षमदितिर्माता स पिता स पुत्र: । विश्वे देवाघअदितिः पश्न जना5अदितिज्जतिमदितिर्जनित्वमू
- **Translation**: 

---

### Verse 13 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.33)
- **Original**: दीघयुत्वाय बलाय वर्चसे सुप्रजास्त्वाय सहसा । अथो जीव शरदः शतमू
- **Translation**: 

---

### Verse 14 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.34)
- **Original**: ऊँ घौः शान्तिरन्तरिक्षथ शान्ति: पूथिवी शन्तिरापः शान्तिरोधधय: शान्ति: वनस्पतयः शान््ति्विश्विदेवा: शान्तिर्ब्रह्म शान्ति: सर्वे शान्ति: शान्तिरेव शान्ति सा मा शान्तिरेधि
- **Translation**: 

---

### Verse 15 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.35)
- **Original**: विश्वानि देव सवितर्दुरितानि परासुव यद्भद्वंतन्न आसुव
- **Translation**: 

---

### Verse 16 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.36)
- **Original**: श्री विश्वकर्मा पुराण एवं पूजन पद्धति भ्
- **Translation**: 

---

### Verse 17 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.37)
- **Original**: यतो यतः समीहसे ततो नो 5अभयं कुरु । शत्नः कुरुप्प्रजाम्योउसयन्नः पशुभ्यः । शान्ति: शान्ति: सुशान्तिर्मवतु
- **Translation**: 

---

### Verse 18 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.38)
- **Original**: ः इस प्रकार स्वस्त्ययन के बाद आचार्य (कर्मकाण्डी) अक्षत छिड़के तथा हाथ में फूल देकर यजमान को हाथ जोड़ने को कहे और स्वयं पुनः देवताओं की प्रार्थना करे- श्ीमन्महागणाधिपतये नमः
- **Translation**: 

---

### Verse 19 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.39)
- **Original**: . श्रीलक्ष्मीनारायणाभ्यां... नमः । वाणीहिरण्यगभ्यां नमः । उसामहेश्वराम्यां नमः । शचीपुरन्दराभ्यां नमः । धर्माय नमः । वास्तुदेवाय नमः । विश्वकर्मणे नमः । कुलदेवताभ्यो नमः । इष्टदेवंताभ्यो नमः । स्थानदेवताप्यो नमः सर्वेश्यो देवेग्यी नमो नमः । संवश्यो देवीस्यो नमः । अथ तांत्रिकमतेन देवताध्यानमू विशवेश॑. माधवं... दुरण्टि. दण्डपाणिश्न भैरवमू । वन्दे काशी गुहां गज्नां सवानी मणिकर्णिकामू
- **Translation**: 

---

### Verse 20 (Vishva Karma Puran And Pujan Paddhati By Pd Rakesh Shastri 0.40)
- **Original**: त्रिवेणीं. माघवं शम्मुं. भरद्वाजश्ल वासुकीमू । वन्देउक्षयवटं . शेष. प्रयाग तीर्धनायकमू
- **Translation**: 

---

